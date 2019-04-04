#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys
import configparser
import datetime
import io
import pymysql
import logging
import re
import textwrap
import requests
import time
import numpy as np 
import traceback
from decimal import * 
import json
from common import Common

getcontext().prec = 10

class common() :
	MySqlConn = None
	GatewayName = 'BoundaryScan Fail Check'

commonObj = common()
with open('data.json' , 'r') as reader:
    jf = json.loads(reader.read())
# 維修代碼
ErrCode = jf['ErrCode']

def main() :
	config = configparser.RawConfigParser()
	config.read('./config.cfg')
	if not os.path.exists('./Log'):
		os.makedirs('./Log')
	logging.basicConfig(filename='./Log/'+datetime.datetime.today().strftime("%Y%m%d")+'.log'
		, level=logging.INFO
		, format='%(asctime)s %(message)s'
		, datefmt='%Y/%m/%d %I:%M:%S %p')
	try :
		commonObj.MySqlConn = pymysql.connect(host=config.get('ICT_Exp','mysqlserver')
			,user=config.get('ICT_Exp','mysqluser')
			,passwd=config.get('ICT_Exp','mysqlpassword')
			,db=config.get('ICT_Exp','database')
			,charset='utf8')
	except Exception as inst:
		print('MySql Connection Fail')
		print(inst)
		logging.error('{0} happen MySql Connection Fail'.format(commonObj.GatewayName))
		logging.error(inst)
	
def Fetch() :
	aStart = time.time()#計時開始
	if commonObj.MySqlConn == None :
		print('No Db Conn')
		return None
	logging.info('{0} Start'.format(commonObj.GatewayName))
	print('{0} Start'.format(commonObj.GatewayName))
	stored_LL = {}			#儲存已計算的良率
	now = datetime.datetime.now()		 	#獲取當前時間
	day1 = datetime.timedelta(days=1) 	#只計算前一天的資料
	day90 = datetime.timedelta(days=90) 	#90天前的紀錄不予理會
	today_begin = now.strftime("%Y-%m-%d") + " 00:00:00"
	today = now.strftime("%Y-%m-%d") + " 23:59:59"		#轉字串
	today_90 = (now-day90).strftime("%Y-%m-%d") + " 00:00:00"  #計算90天前的時間
	dateTmp01 = '2019-03-10 00:00:00'
	dateTmp02 = '2019-03-17 00:00:00'
	yesterday = (now - day1).strftime("%Y-%m-%d") + " 00:00:00"
	tomorrow = (now + day1).strftime("%Y-%m-%d") + " 00:00:00"

	StartTime = today_begin
	EndTime = today
	CPK_90day = (datetime.datetime.strptime(EndTime, '%Y-%m-%d %H:%M:%S')-day90).strftime("%Y-%m-%d") + " 00:00:00"

	FulearnCur = commonObj.MySqlConn.cursor()
	#抓取fail資料(測試步驟Fail)
	FulearnCur.execute(textwrap.dedent('''
		SELECT a.*,b.mfg FROM `boundary_scan_result` a 
		LEFT JOIN tb_fixture b ON a.board = b.pn
		WHERE status = 1 AND end_time BETWEEN '{0}' AND '{1}'
		GROUP BY `sn`,`component` ORDER BY `end_time` ASC
		'''.format(StartTime,EndTime)))
	SqlList = []
	debug = []
	# print (FulearnCur.rowcount)
	for row in FulearnCur :
		machine = row[0]
		sn = row[1]
		component = row[2]
		status = row[3]
		end_time = row[4]
		seq = row[5]
		board = row[6]
		BU = row[7]
		sfc_repair = 0
		label = '？？？'
		label_no = 999			#label編號: 0-無維修紀錄 1-零件或製程問題 2-程式不穩定 3-探針或接觸問題 4-零件與維修記錄無法匹配 5-找不到重測紀錄 6-wirelist查無資料 7-重測失敗
		isDone = False			#邏輯判斷結束
		isMatch = False			#FailSymptom是否一致
		isNDF = False 			#是否NPF
		debugRow = sn +' '+ component +': '			#追蹤流程走向
		min5 = datetime.timedelta(minutes=5) 	#匹配api資料內和資料庫的時間差（相差5分內的極大可能為同一資料）
		min1 = datetime.timedelta(minutes=1)
		componentcode = ''		# 零件料號
		vendorcode = ''			# Vendor
		datacode = ''			# DC
		lotcode = ''			# LC
		ErrorCode = ''			# Error Code
		BUname = ''
		# now = datetime.datetime.now()  	#獲取當前時間
		if end_time > (now - day90):
			debugRow = debugRow + 'in90d -> '
			#查詢SFC是否有fail紀錄
			retries = 0			#連接api時失敗重試
			success = False
			while retries < 7 and not success:
				try:
					if BU == 'MFGI': BUname = 'UAG'
					elif BU == 'MFGII': BUname = 'SRG'
					elif BU == 'MFGIII': BUname = 'UCEBU'
					elif BU == 'MFGV': BUname = 'ERBU'
					elif BU == 'MFGVI': BUname = 'WNBU'
					elif BU == 'MFGVII': BUname = 'SAVBU'
					elif BU == 'MFGVIII': BUname = 'SFPG'
					else: BUname = 'UAG'
					r = requests.get('http://10.157.20.101:8083/Api/fail?sn='+sn+'&BU='+BUname)
					if r.status_code == requests.codes.ok : success = True
					SFC_fail = r.json() 
				except Exception as err:
					retries += 1
					print(r.raise_for_status()) 
					if retries == 7 : break
			sameSymptom = False
			has_record=False 	#是否有維修紀錄
			for fail_info in SFC_fail['data'] :
				debugRow = debugRow + '(' + fail_info['Repair']['FailSymptom'] +"("+fail_info['Repair']['Createdate']+')/('+str(end_time)+'))'
				#判定Fail Symptom是否一致
				if fail_info['Repair']['FailSymptom'] == 'failed digital or boundary scan test' \
				and datetime.datetime.strptime(fail_info['Repair']['Createdate'], '%Y-%m-%d %H:%M:%S') > end_time-min5 :
					sameSymptom = True
			if sameSymptom is True: 
				debugRow = debugRow + 'same Symptom -> '
				#SFC查找紀錄(有fail紀錄)
				SFC_fail=[]
				Retest_Pass = False	#重測是否通過
				isMatch = True
				retries = 0			#連接api時失敗重試
				success = False
				SFC_result = {}
				while retries < 7 and not success:
					try:
						if BU == 'MFGI': BUname = 'UAG'
						elif BU == 'MFGII': BUname = 'SRG'
						elif BU == 'MFGIII': BUname = 'UCEBU'
						elif BU == 'MFGV': BUname = 'ERBU'
						elif BU == 'MFGVI': BUname = 'WNBU'
						elif BU == 'MFGVII': BUname = 'SAVBU'
						elif BU == 'MFGVIII': BUname = 'SFPG'
						else: BUname = 'UAG'
						r = requests.get('http://10.157.20.101:8083/Api/repair?sn='+sn+'&BU='+BUname)
						if r.status_code == requests.codes.ok : success = True
						SFC_result = r.json() 
					except Exception as err:
						retries += 1
						print(r.raise_for_status()) 
						if retries == 7 : break
				try:
					failurecode = ''
					failLocation = ''
					for repair_info in SFC_result['data'] :
						if repair_info['Repair']['Rootcause'] == '':
							debugRow = debugRow + 'no record -> '
							#沒有維修紀錄(沒維修或記錄已被清除(超過90天))
							has_record = False
							label = '無維修紀錄'
							label_no = 0
						elif datetime.datetime.strptime(repair_info['Repair']['Createdate'], '%Y-%m-%d %H:%M:%S') > end_time-min5 :
							has_record = True
							sfc_repair = 1
							componentcode = repair_info['Repair']['Componentcode']
							vendorcode = repair_info['Repair']['Vendorcode']
							datacode = repair_info['Repair']['Datacode']
							lotcode = repair_info['Repair']['Lotcode']
							ErrorCode = repair_info['Repair']['FailureCode']
							failurecode = repair_info['Repair']['Rootcause']
							failLocation = repair_info['Repair']['Location']
							# print ('failurecode: ' + failurecode + ' -> ' + ErrCode[failurecode])

					if failurecode == '' :
						debugRow = debugRow + 'no record -> '
						#沒有維修紀錄(沒維修或記錄已被清除(超過90天))
						has_record = False
						label = '無維修紀錄'
						label_no = 0
						# print(label)
						# noRecord_Day += 1
					elif ErrCode[failurecode] != 'NDF':
						debugRow = debugRow + 'not NDF(' + failurecode + ') -> '
						# 判斷維修零件是否符合錯誤紀錄
						if failLocation.lower() == component.split('_')[0] :
							debugRow = debugRow + 'component match -> '
							isNDF = False
							label = '零件或製程問題'
							label_no = 1
							# print(label)
						else :
							debugRow = debugRow + 'component no match -> '
							isNDF = True 
							label = '零件與維修紀錄無法匹配'
							label_no = 4
							# print(label)
					else: isNDF = True
				except Exception as err:
					traceback.print_exc()
			else:	
				#找不到fail紀錄 or FailSymptom不一致
				debugRow = debugRow + 'no match Symptom -> '
			if has_record is False and sameSymptom is True:
				label = '無維修紀錄'
				label_no = 0
			#找不到fail紀錄 or FailSymptom不一致 or NPF
			elif sameSymptom is False or isNDF is True:
				debugRow = debugRow + 'find re-test -> '
				#查找是否重測
				Retest_Pass = False
				findRetest = commonObj.MySqlConn.cursor()
				findRetest.execute(textwrap.dedent('''
					SELECT * FROM `boundary_scan_result`
					WHERE board='{0}' AND sn = '{1}' AND component = '{2}' AND end_time > '{3}'
					AND end_time BETWEEN '{4}' AND '{5}'
					GROUP BY end_time ORDER BY `end_time`,`seq` ASC
					'''.format(board,sn,component,end_time,StartTime,EndTime)))
				isDone = False		#邏輯判斷結束
				re_sn = ''
				re_time = ''
				if findRetest.rowcount == 0 :   #沒有重測 or SQL query錯誤
					debugRow = debugRow + 'no re-test -> '
					label = '找不到重測紀錄'
					label_no = 5
					# print(label)
				else :			#重測有資料
					for line in findRetest :
						#查找重測是否成功
						re_sn = line[1]
						re_component = line[2]
						re_status = line[3]    #block_status
						re_time = line[4]
						no_ShareBRC = False
						program_unstable = False
						if re_status == '0' : 
							Retest_Pass = True
					if Retest_Pass is True:
						# 查找testjet是否有測試
						dd3vice = component.split('_')
						findTestjet = commonObj.MySqlConn.cursor()
						findTestjet.execute(textwrap.dedent('''
							SELECT * FROM `testjet_result`
							WHERE board='{0}' AND sn = '{1}' AND device = '{2}'
							AND end_time BETWEEN '{3}' AND '{4}'
							GROUP BY `sn`
							'''.format(board,sn,dd3vice[0],StartTime,EndTime)))
						if findTestjet.rowcount == 0:
							#計算良率
							if component in stored_LL:
								liang_lu = stored_LL[component]
								if liang_lu <= 0.05:
									label = '感應面板或探針問題 (' + str(1-liang_lu) + ')'
									label_no = 3
								else:
									label = '程式問題 (' + str(1-liang_lu) + ')'
									label_no = 2
							else:
								countTotal = commonObj.MySqlConn.cursor()
								countTotal.execute(textwrap.dedent('''
									SELECT * FROM `boundary_scan_result`
									WHERE board='{0}' AND component = '{1}' AND end_time BETWEEN '{2}' AND '{3}'
									Group by end_time ORDER BY `end_time`,`seq` ASC
									'''.format(board,component,StartTime,EndTime)))
								countFail = commonObj.MySqlConn.cursor()
								countFail.execute(textwrap.dedent('''
									SELECT * FROM `boundary_scan_result`
									WHERE board='{0}' AND component = '{1}' AND end_time BETWEEN '{2}' AND '{3}' AND status != 0
									Group by end_time ORDER BY `end_time`,`seq` ASC
									'''.format(board,component,StartTime,EndTime)))
								liang_lu = 1 - (countFail.rowcount/countTotal.rowcount)
								# print('良率：' + str(liang_lu))
								stored_LL[component] = liang_lu
								if liang_lu > 0.99:			
									label = '探針或測試點接觸問題' + '(' + str(liang_lu) + ')'
									label_no = 3
								else:
									label = '程式問題' + '(' + str(liang_lu) + ')'
									label_no = 2
						else: 
							label = '程式問題'
							label_no = 2
					else: 
						debugRow = debugRow + 're-test fail -> '
						label = "重測失敗"
						label_no = 7
						# print(label)
						# retest_fail += 1
				findRetest.close()
			#寫入資料表
			SqlList.append(textwrap.dedent('''
				INSERT IGNORE INTO label (logic_type,seq,sn,label,label_no,board,componentcode,vendorcode,datacode,lotcode,failurecode,end_time) 
				VALUES ('boundary scan','{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}')
				ON DUPLICATE KEY UPDATE label = '{2}',label_no = '{3}';
				'''.format(seq,sn,label,label_no,board,componentcode,vendorcode,datacode,lotcode,ErrorCode,end_time)))
		debugRow = debugRow + 'done\n'
		debug.append(debugRow)

	with open('./Output.sql' ,'wb') as f:
		f.write(bytearray(''.join(SqlList),"utf-8"))
		f.close()
	with open('./Seqence.txt' ,'wb') as fo:
		fo.write(bytearray(''.join(debug),"utf-8"))
		fo.close()

	FulearnCur.close()
	
	#程式執行前先清空舊資料
	# truncate = commonObj.MySqlConn.cursor()
	# truncate.execute(textwrap.dedent('''
	# 	DELETE FROM label WHERE logic_type = 'boundary scan'
	# 	'''))
	# truncate.close()

	Cur = commonObj.MySqlConn.cursor()
	for update in SqlList:
		Cur.execute(update)
		commonObj.MySqlConn.commit()
	Cur.close()
	aEnd = time.time()#計時結束
	print ("===== All cost %f sec =====" % (aEnd - aStart))
	commonObj.MySqlConn.close()
	logging.info('{0} Finish'.format(commonObj.GatewayName))
	print('{0} Finish'.format(commonObj.GatewayName))
	
	
main()
Fetch()