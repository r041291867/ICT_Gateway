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
	GatewayName = 'Analog Powered Fail Check'

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
	stored_sn = []			#儲存有問題的sn
	stored_component = []	#儲存已計算的零件
	stored_CPK = {}			#儲存已計算的CPK
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
		SELECT a.*,b.BU FROM analog_powered_result a 
		LEFT JOIN board_info b ON a.board = b.board WHERE status = 1
		AND end_time BETWEEN '{0}' AND '{1}'
		GROUP BY `sn`,`component`,`test_condition` ORDER BY `end_time` ASC
		'''.format(StartTime,EndTime)))
	SqlList = []
	debug = []
	# print (FulearnCur.rowcount)
	for row in FulearnCur :
		machine = row[0]
		sn = row[1]
		block_status = row[2]
		component = row [3]
		status = row[4]
		measured = row[5]
		test_condition = row[6]
		limit_type = row[7]
		nominal = row[8]
		high_limit = row[9]
		low_limit = row[10]
		end_time = row[11]
		seq = row[12]
		board = row[13]
		BU = row[14]
		sfc_repair = 0
		label = '？？？'
		label_no = 999			#label編號: 0-無維修紀錄 1-零件或製程問題 2-程式不穩定 3-探針或接觸問題 4-零件與維修記錄無法匹配 5-找不到重測紀錄 6-wirelist查無資料 7-重測失敗
		isDone = False			#邏輯判斷結束
		isMatch = False			#FailSymptom是否一致
		isNDF = False 			#是否NPF
		debugRow = sn +' '+ component +' '+ test_condition +': '			#追蹤流程走向
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
				if fail_info['Repair']['FailSymptom'] == 'failed functional test' \
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
						isNDF = False
						stored_sn.append(sn)
						label = '零件或製程問題'
						label_no = 1
							# print(label)
					else: isNDF = True
				except Exception as err:
					traceback.print_exc()
			else:	
				debugRow = debugRow + 'no match Symptom -> '
				#找不到fail紀錄 or FailSymptom不一致
				
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
					SELECT * FROM analog_powered_result
					WHERE board='{0}' AND `sn` = '{1}' AND `component` = '{2}' AND `test_condition` = '{3}' AND end_time > '{4}'
					AND end_time BETWEEN '{5}' AND '{6}'
					GROUP BY `end_time` ORDER BY `end_time` ASC
					'''.format(board,sn,component,test_condition,end_time,StartTime,EndTime)))
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
						re_test_condition = line[6]
						re_status = line[2]    #block_status
						re_time = line[11]
						no_ShareBRC = False
						program_unstable = False
						if re_status == '00' : 
							Retest_Pass = True
					if Retest_Pass is True:
						#計算CPK
						CPK = 0
						component_combine = component+'|'+test_condition+'|'+board
						if component_combine in stored_CPK:
							CPK = stored_CPK[component_combine]
							if CPK > 0.67 : 
								stored_sn.append(sn)
								label = '探針或測試點接觸問題(' + str(CPK) + ')' 
								label_no = 3
							else : 
								label = '程式不穩定(' + str(CPK) + ')'
								label_no = 2
							# print(label)
						else:
							# print('===Count CPK===')
							# t1 = time.time()
							stored_component.append(component_combine)
							countCPK = commonObj.MySqlConn.cursor()
							countCPK.execute(textwrap.dedent('''
								SELECT * FROM analog_powered_result
								WHERE board='{0}' AND component = '{1}' AND test_condition = '{2}' 
								AND end_time BETWEEN '{3}' AND '{4}' ORDER BY `end_time` ASC
								'''.format(board,component,test_condition,CPK_90day,EndTime)))
							# t2 = time.time()
							# print('======find cpk use %f sec =====' % (t2 - t1))
							T = []
							nominal = 0
							HighAndLow = []
							total = []
							for data in countCPK:
								if (data[5] >= 0 and data[5] <= (data[9] + data[10])/2 + abs(data[9] - data[10])*5):		#篩選掉明顯有問題的資料
									if (data[9]-data[10]) != 0:
										T.append(data[9]-data[10])
									HighAndLow.append(data[9]+data[10])
									nominal = data[8]
									total.append(data[5])
							MEAN = np.mean(total)
							VAR = np.std(total)
							if nominal is None : 
								nominal = HighAndLow[0]/2
							# if T[0] == 0 or T[0] is None :
							# 	break
							CA = abs((MEAN - nominal)/(T[0]/2))
							CP = T[0]/(VAR*6)
							CPK = (1-CA)*(CP)
							stored_CPK[component_combine] = CPK
							isDone = True
							# t3 = time.time()
							# print('======count use %f sec =====' % (t3 - t2))
							# print('CPK = ' + str(CPK) + '\n')
							if CPK > 0.67 : 
								stored_sn.append(sn)
								label = '探針或測試點接觸問題(' + str(CPK) + ')' 
								label_no = 3
							else : 
								#CPK小於0.67則再用上下限做中心值再算一次
								nominal = HighAndLow[0]/2
								CA = abs((MEAN - nominal)/(T[0]/2))
								CP = T[0]/(VAR*6)
								CPK = (1-CA)*(CP)
								stored_CPK[component_combine] = CPK
								if CPK > 0.67 : 
									stored_sn.append(sn)
									label = '探針或測試點接觸問題(' + str(CPK) + ')' 
									label_no = 3
								else:
									label = '程式不穩定(' + str(CPK) + ')'
									label_no = 2
								# print(label)
							countCPK.close()
					else: 
						debugRow = debugRow + 're-test fail -> '
						label = "重測失敗"
						label_no = 7
						# print(label)
						# retest_fail += 1
				findRetest.close()
			#寫入資料表
			SqlList.append(textwrap.dedent('''
				INSERT IGNORE INTO label (logic_type,seq,sn,test_condition,label,label_no,board,componentcode,vendorcode,datacode,lotcode,failurecode,end_time) 
				VALUES ('analog powered','{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')
				ON DUPLICATE KEY UPDATE label = '{3}',label_no = '{4}';
				'''.format(seq,sn,test_condition,label,label_no,board,componentcode,vendorcode,datacode,lotcode,ErrorCode,end_time)))
		debugRow = debugRow + 'done\n'
		debug.append(debugRow)

	with open('./Output.sql' ,'wb') as f:
		f.write(bytearray(''.join(SqlList),"utf-8"))
		f.close()
	with open('./Seqence_APo.txt' ,'wb') as fo:
		fo.write(bytearray(''.join(debug),"utf-8"))
		fo.close()

	stored_sn_new = list(set(stored_sn))
	stored_component_new = list(set(stored_component))
	stored_CPK_II = {}
	# print('===Count CPK Twice===')
	for CPK_twice in stored_component_new:
		#計算第二次CPK
		CPK = 0
		countCPK = commonObj.MySqlConn.cursor()
		sp = CPK_twice.split('|')
		countCPK.execute(textwrap.dedent('''
			SELECT * FROM analog_powered_result
			WHERE board='{0}' AND component = '{1}' AND test_condition = '{2}' 
			AND end_time BETWEEN '{3}' AND '{4}' ORDER BY `end_time` ASC
			'''.format(sp[2],sp[0],sp[1],CPK_90day,EndTime)))
		T = []
		nominal = 0
		HighAndLow = []
		total = []
		for data in countCPK:
			sn2 = data[1]
			measured2 = data[5]
			nominal2 = data[8]
			high_limit2 = data[9]
			low_limit2 = data[10]
			if sn2 not in stored_sn:
				if (measured2 >= 0 and measured2 <= (high_limit2 + low_limit2)/2 + abs(high_limit2 - low_limit2)*5):		#篩選掉明顯有問題的資料
					if (high_limit2-low_limit2) != 0:
						T.append(high_limit2-low_limit2)
					HighAndLow.append(high_limit2+low_limit2)
					nominal = nominal2
					total.append(measured2)
		MEAN = np.mean(total)
		VAR = np.std(total)
		if nominal is None : 
			nominal = HighAndLow[0]/2
		# if T[0] == 0 or T[0] is None :
		# 	break
		CA = abs((MEAN - nominal)/(T[0]/2))
		CP = T[0]/(VAR*6)
		CPK = (1-CA)*(CP)
		isDone = True

		SqlList.append(textwrap.dedent('''
			UPDATE label SET cpk = '{0}' WHERE component ='{1}' AND test_condition = '{2}' AND board = '{3}';
			'''.format(CPK,sp[0],sp[1],sp[2])))

		countCPK.close()
	# print('===Count CPK Done===')
	FulearnCur.close()
	
	#程式執行前先清空舊資料
	# truncate = commonObj.MySqlConn.cursor()
	# truncate.execute(textwrap.dedent('''
	# 	DELETE FROM label WHERE logic_type = 'analog powered'
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