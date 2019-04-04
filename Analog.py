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

getcontext().prec = 13

class common() :
	MySqlConn = None
	GatewayName = 'Analog Fail Check'

commonObj = common()
with open('data.json' , 'r') as reader:
    jf = json.loads(reader.read())
# 維修代碼
ErrCode = jf['ErrCode']
#零件誤差容許值
high_tolerance = jf['high_tolerance']
low_tolerance = jf['low_tolerance']

# 判斷是否NaN
def isNaN(num):
    return num != num

def InTolerance(test_type,mean,nominal):
	# 根據誤差表判斷是否在誤差範圍內
	in_tolerance = False
	if isNaN(mean) is False:
		if test_type == 'A-RES':
			if nominal <= 10:
				if mean <= Decimal.from_float(16.5):
					in_tolerance = True
			elif nominal <= 20:
				if mean <= nominal * Decimal.from_float(high_tolerance[test_type]['20'])\
				and mean >= nominal * Decimal.from_float(low_tolerance[test_type]['20']):
					in_tolerance = True
			elif nominal <= 35:
				if mean <= nominal * Decimal.from_float(high_tolerance[test_type]['35'])\
				and mean >= nominal * Decimal.from_float(low_tolerance[test_type]['35']):
					in_tolerance = True
			elif nominal <= 300:
				if mean <= nominal * Decimal.from_float(high_tolerance[test_type]['300'])\
				and mean >= nominal * Decimal.from_float(low_tolerance[test_type]['300']):
					in_tolerance = True
			elif nominal <= 1000:
				if mean <= nominal * Decimal.from_float(high_tolerance[test_type]['1000'])\
				and mean >= nominal * Decimal.from_float(low_tolerance[test_type]['1000']):
					in_tolerance = True
			elif nominal <= 10000:
				if mean <= nominal * Decimal.from_float(high_tolerance[test_type]['10000'])\
				and mean >= nominal * Decimal.from_float(low_tolerance[test_type]['10000']):
					in_tolerance = True
			elif nominal <= 50000:
				if mean <= nominal * Decimal.from_float(high_tolerance[test_type]['50000'])\
				and mean >= nominal * Decimal.from_float(low_tolerance[test_type]['50000']):
					in_tolerance = True
			elif nominal <= 100000:
				if mean <= nominal * Decimal.from_float(high_tolerance[test_type]['100000'])\
				and mean >= nominal * Decimal.from_float(low_tolerance[test_type]['100000']):
					in_tolerance = True
			elif nominal <= 1000000:
				if mean <= nominal * Decimal.from_float(high_tolerance[test_type]['1000000'])\
				and mean >= nominal * Decimal.from_float(low_tolerance[test_type]['1000000']):
					in_tolerance = True
			else:
				if mean <= nominal * Decimal.from_float(high_tolerance[test_type]['1000001'])\
				and mean >= nominal * Decimal.from_float(low_tolerance[test_type]['1000001']):
					in_tolerance = True
		elif test_type == 'A-CAP':
			if nominal*(10**12) <= 33:
				if mean <= nominal*(10**12) * Decimal.from_float(high_tolerance[test_type]['33'])\
				and mean >= nominal*(10**12) * Decimal.from_float(low_tolerance[test_type]['33']):
					in_tolerance = True
			elif nominal*(10**12) <= 200:
				if mean <= nominal*(10**12) * Decimal.from_float(high_tolerance[test_type]['200'])\
				and mean >= nominal*(10**12) * Decimal.from_float(low_tolerance[test_type]['200']):
					in_tolerance = True
			elif nominal*(10**12) <= 1000:
				if mean <= nominal*(10**12) * Decimal.from_float(high_tolerance[test_type]['1000'])\
				and mean >= nominal*(10**12) * Decimal.from_float(low_tolerance[test_type]['1000']):
					in_tolerance = True
			elif nominal*(10**12) <= 2000:
				if mean <= nominal*(10**12) * Decimal.from_float(high_tolerance[test_type]['2000'])\
				and mean >= nominal*(10**12) * Decimal.from_float(low_tolerance[test_type]['2000']):
					in_tolerance = True
			elif nominal*(10**12) <= 15900000:
				if mean <= nominal*(10**12) * Decimal.from_float(high_tolerance[test_type]['15900000'])\
				and mean >= nominal*(10**12) * Decimal.from_float(low_tolerance[test_type]['15900000']):
					in_tolerance = True
			elif nominal*(10**12) <= 10000000000:
				if mean <= nominal*(10**12) * Decimal.from_float(high_tolerance[test_type]['10000000000'])\
				and mean >= nominal*(10**12) * Decimal.from_float(low_tolerance[test_type]['10000000000']):
					in_tolerance = True
			else:
				if mean <= nominal*(10**12) * Decimal.from_float(high_tolerance[test_type]['10000000001'])\
				and mean >= nominal*(10**12) * Decimal.from_float(low_tolerance[test_type]['10000000001']):
					in_tolerance = True
	return in_tolerance

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
		SELECT a.machine,a.sn,a.block_status,a.component,a.test_type,a.`status`,a.test_condition,a.end_time,a.seq,a.board,b.mfg
		FROM analog_result a LEFT JOIN tb_fixture b ON a.board = b.pn
		WHERE `status` = 1  AND end_time BETWEEN '{0}' AND '{1}'
		GROUP BY `sn`,`component`,`test_type`,test_condition 
		ORDER BY `end_time` ASC,`seq` ASC
		'''.format(StartTime,EndTime)))
	SqlList = []
	debug = []
	print (FulearnCur.rowcount)
	for row in FulearnCur :
		machine = row[0]
		sn = row[1]
		block_status = row[2]
		component = row[3]
		test_type = row[4]
		status = row[5]	
		# measured = row[6]
		test_condition = row[6]
		# limit_type = row[8]
		# nominal = row[9]
		# high_limit = row[10]
		# low_limit = row[11]
		end_time = row[7]
		seq = row[8]
		board = row[9]
		BU = row[10]
		sfc_repair = 0
		label = '？？？'
		label_no = 999			#label編號: 0-無維修紀錄 1-零件或製程問題 2-程式不穩定 3-探針或接觸問題 4-零件與維修記錄無法匹配 5-找不到重測紀錄 6-wirelist查無資料 7-重測失敗
		isDone = False			#邏輯判斷結束
		isMatch = False			#FailSymptom是否一致
		isNDF = False 			#是否NPF
		debugRow = sn +' '+ component +' '+ test_type + str(end_time) + ': '			#追蹤流程走向
		min5 = datetime.timedelta(minutes=5) 	#匹配api資料內和資料庫的時間差（相差5分內的極大可能為同一資料）
		min1 = datetime.timedelta(minutes=1)
		componentcode = ''		# 零件料號
		vendorcode = ''			# Vendor
		datacode = ''			# DC
		lotcode = ''			# LC
		ErrorCode = ''			# Error Code
		BUname = ''
		if end_time > (now - day90):
			debugRow = debugRow + 'in90d '+str(now)+' -> '
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
				if fail_info['Repair']['FailSymptom'] == 'failed analog test' \
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
					elif ErrCode[failurecode] != 'NDF':
						debugRow = debugRow + 'not NDF(' + failurecode + ') -> '
						# 判斷維修零件是否符合錯誤紀錄
						if failLocation.lower() == component.split('%')[0] :
							debugRow = debugRow + 'component match -> '
							isNDF = False
							stored_sn.append(sn)
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
					SELECT * FROM analog_result WHERE `sn` = '{0}' AND `component` = '{1}' AND test_type = '{2}' AND end_time >= '{3}'
					AND end_time BETWEEN '{4}' AND '{5}' AND board = '{6}'
					ORDER BY `seq` ASC
					'''.format(sn,component,test_type,end_time,StartTime,EndTime,board)))
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
						re_component = line[3]
						re_status = line[5]    #not block_status
						re_time = line[12]
						no_ShareBRC = False
						program_unstable = False
						if re_status == '0' : 
							Retest_Pass = True
					if Retest_Pass is True:
						debugRow = debugRow + 're-test pass -> '
						#找出該零件的針點
						WireList = commonObj.MySqlConn.cursor()
						WireList.execute(textwrap.dedent('''
							SELECT * FROM `wirelist` WHERE `board` = '{0}' AND `component` = '{1}' and test_type = 'analog' and (mark = 's' or mark = 'i')
							'''.format(board,re_component)))
						sharedBRC = []			#儲存BRC已便查詢共用針點
						sharedBRCcomponent = []	#儲存針點的零件以便查詢共用針點的sn
						#找出針點共用零件
						if WireList.rowcount == 0:
							label = 'Wirelist查無資料'
							label_no = 6
							no_ShareBRC = True
							# print(label)
							# break
						else: 
							for wire in WireList :
								wire_component = wire[2]
								wire_BRC = wire[5]
								sharedBRC.append(wire_BRC)
							for BRC in sharedBRC:
								# 查找共用點是否超過10個
								FindPWR = commonObj.MySqlConn.cursor()
								FindPWR.execute(textwrap.dedent('''
									SELECT * FROM `wirelist` WHERE `board` = '{0}' AND `BRC` = '{1}' AND component != '{2}' and test_type = 'analog' and (mark = 's' or mark = 'i')
									'''.format(board,BRC,component)))
								if FindPWR.rowcount >= 10 :
									FindPWR.close()
									no_ShareBRC = True
									break
							if no_ShareBRC is False:
								ShareBRC = commonObj.MySqlConn.cursor()
								ShareBRC.execute(textwrap.dedent('''
									SELECT *,count(*) FROM (
									SELECT * FROM `wirelist` WHERE `board` = '{0}' AND `BRC` = '{1}' AND component != '{2}' and test_type = 'analog' and (mark = 's' or mark = 'i')
									UNION ALL
									SELECT * FROM `wirelist` WHERE `board` = '{0}' AND `BRC` = '{3}' AND component != '{2}' and test_type = 'analog' and (mark = 's' or mark = 'i')
									) a
									GROUP BY board,test_type,component,subtest
									HAVING COUNT(*)>1
									'''.format(board,sharedBRC[0],component,sharedBRC[1])))
								if ShareBRC.rowcount == 0 : 
									#找不到共用針點則直接挑出
									no_ShareBRC = True		#沒有共用針點
									# break
								else:
									for other_wire in ShareBRC:
										other_component = other_wire[2]
										#儲存零件
										sharedBRCcomponent.append(other_component) 
								ShareBRC.close()
							#使用個別零件尋找其他sn
							if no_ShareBRC is False:
								for BRC in sharedBRCcomponent:
									findSN = commonObj.MySqlConn.cursor()
									findSN.execute(textwrap.dedent('''
										SELECT `block_status` FROM analog_result
										where component = '{0}' and sn = '{1}' AND board = '{2}'
										AND end_time BETWEEN '{3}' AND '{4}'
										ORDER BY `end_time` ASC, `seq` ASC
										'''.format(BRC,sn,board,StartTime,EndTime)))
									if findSN.rowcount == 0:
										#有查到共用針點但是沒有測試結果
										no_ShareBRC = True
										break

									else :
										for findSN_result in findSN :
											#一次PASS則結束
											if findSN_result[0] == '00':
												program_unstable = True
												label = '程式不穩定'
												label_no = 2
												# print(label)
												break
									if program_unstable is True: 
										break
									else :
										stored_sn.append(sn)
										label = '探針或測試點接觸問題'
										label_no = 3
										# print(label)
									findSN.close()
						if no_ShareBRC is True :
							#計算CPK
							CPK = 0
							component_combine = component+'|'+test_type+'|'+test_condition+'|'+board
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
								try:
									stored_component.append(component_combine)
									countCPK = commonObj.MySqlConn.cursor()
									countCPK.execute(textwrap.dedent('''
										SELECT * FROM analog_result
										WHERE component = '{0}' AND test_type = '{1}' AND test_condition = '{2}'
										AND end_time BETWEEN '{3}' AND '{4}' AND board = '{5}'
										ORDER BY `end_time` ASC
										'''.format(re_component,test_type,test_condition,CPK_90day,EndTime,board)))
									T = []
									nominal = 0
									HighAndLow = []
									total = []

									for data in countCPK:
										measured2 = data[6]
										nominal2 = data[9]
										high_limit2 = data[10]
										low_limit2 = data[11]
										if (abs(measured2) <= (high_limit2 + low_limit2)/2 + abs(high_limit2 - low_limit2)*5):		#篩選掉明顯有問題的資料
											if (high_limit2-low_limit2) != 0:
												T.append(high_limit2-low_limit2)
											HighAndLow.append(high_limit2+low_limit2)
											nominal = nominal2
											total.append(measured2)
									MEAN = np.mean(total)
									VAR = np.std(total)
									if nominal is None : 
										nominal = HighAndLow[0]/2
									if T is not None :
										CA = abs((MEAN - nominal)/(T[0]/2))
										CP = T[0]/(VAR*6)
										CPK = (1-CA)*(CP)
										stored_CPK[component_combine] = CPK
										isDone = True
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
								except:
									print(sn +' '+ component +' '+ test_type)
									traceback.print_exc()
						WireList.close()
					else: 
						debugRow = debugRow + 're-test fail -> '
						label = "重測失敗"
						label_no = 7
						# print(label)
						# retest_fail += 1
				findRetest.close()
			#寫入資料表
			SqlList.append(textwrap.dedent('''
				INSERT IGNORE INTO label (logic_type,seq,sn,component,test_type,test_condition,label,label_no,board,componentcode,vendorcode,datacode,lotcode,failurecode,end_time) 
				VALUES ('analog','{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}')
				ON DUPLICATE KEY UPDATE label = '{5}',label_no = '{6}';
				'''.format(seq,sn,component,test_type,test_condition,label,label_no,board,componentcode,vendorcode,datacode,lotcode,ErrorCode,end_time)))
		debugRow = debugRow + 'done\n'
		debug.append(debugRow)
	with open('./Seqence_analog.txt' ,'wb') as fo:
		fo.write(bytearray(''.join(debug),"utf-8"))
		fo.close()
	stored_sn_new = list(set(stored_sn))
	stored_component_new = list(set(stored_component))
	stored_CPK_II = {}
	# print('===Count CPK Twice===')
	for CPK_twice in stored_component_new:
		#計算第二次CPK
		# print(CPK_twice)
		CPK = 0
		countCPK = commonObj.MySqlConn.cursor()
		sp = CPK_twice.split('|')
		countCPK.execute(textwrap.dedent('''
			SELECT * FROM analog_result
			WHERE component = '{0}' AND test_type = '{1}' AND test_condition = '{2}'
			AND end_time BETWEEN '{3}' AND '{4}' AND board = '{5}'
			ORDER BY `end_time` ASC
			'''.format(sp[0],sp[1],sp[2],CPK_90day,EndTime,sp[3])))
		failAVG = 0
		countAVG = []
		T = []
		nominal = 0
		HighAndLow = []
		total = []
		high_limit2 = 0
		try:
			for data in countCPK:
				sn2 = data[1]
				status2 = data[5]
				measured2 = data[6]
				nominal2 = data[9]
				high_limit2 = data[10]
				low_limit2 = data[11]
				if sn2 not in stored_sn_new:
					if (abs(measured2) <= (high_limit2 + low_limit2)/2 + abs(high_limit2 - low_limit2)*5):		#篩選掉明顯有問題的資料
						if (high_limit2-low_limit2) != 0:
							T.append(high_limit2-low_limit2)
						if status2 == '1':
							# print('=========================')
							countAVG.append(measured2)
						HighAndLow.append(high_limit2+low_limit2)
						nominal = nominal2
						total.append(measured2)

			MEAN = np.mean(total)
			failAVG = np.mean(countAVG)
			# print(str(failAVG))
			VAR = np.std(total)
			if nominal is None : 
				nominal = HighAndLow[0]/2
			CA = abs((MEAN - nominal)/(T[0]/2))
			CP = T[0]/(VAR*6)
			CPK = (1-CA)*(CP)
			isDone = True
			# ==============================================
			# if CPK > 0.67 : 
			# 	label = '探針或測試點接觸問題(' + str(CPK) + ')' 
			# 	label_no = 3
			# else : 
			if CPK < 0.67:
				#CPK小於0.67則再用上下限做中心值再算一次
				nominal = HighAndLow[0]/2
				CA = abs((MEAN - nominal)/(T[0]/2))
				CP = T[0]/(VAR*6)
				CPK = (1-CA)*(CP)
				if CPK > 0.67 : 
					# 根據誤差表判斷是否在誤差範圍內
					if (sp[1]=='A-CAP' or sp[1]=='A-RES') :
						in_tolerance = InTolerance(sp[1],failAVG,nominal2)
						if in_tolerance is True:
							label = '程式不穩定(' + str(CPK) + ')'
							label_no = 2
						else:	
							label = '探針或測試點接觸問題(' + str(CPK) + ')' 
							label_no = 3
					else: 
						label = '探針或測試點接觸問題(' + str(CPK) + ')' 
						label_no = 3
				else:
					label = '程式不穩定(' + str(CPK) + ')'
					label_no = 2
			else:
				# 根據誤差表判斷是否在誤差範圍內
				if (sp[1]=='A-CAP' or sp[1]=='A-RES') :
					in_tolerance = InTolerance(sp[1],failAVG,nominal2)
					if in_tolerance is True:
						label = '程式不穩定(' + str(CPK) + ')'
						label_no = 2
					else:	
						label = '探針或測試點接觸問題(' + str(CPK) + ')' 
						label_no = 3
				else:
					label = '探針或測試點接觸問題(' + str(CPK) + ')' 
					label_no = 3
			# ==============================================
				# print(label)
		# print('CPK = ' + str(CPK) + '\n')
		# SqlList.append(textwrap.dedent('''
		# 	UPDATE {0} SET cpk = '{1}' WHERE component = '{2}' AND test_type = '{3}';
		# 	'''.format(TestTB,CPK,sp[0],sp[1])))
			SqlList.append(textwrap.dedent('''
				UPDATE label SET cpk = '{0}',label = '{1}',label_no = '{2}' WHERE label_no = 2 AND component = '{3}' AND test_type = '{4}' AND test_condition = '{5}' AND board = '{6}';
				'''.format(CPK,label,label_no,sp[0],sp[1],sp[2],sp[3])))
		except Exception as err:
			print("⌜"+str(failAVG)+"|"+str(nominal)+"⌝")
			print("⌞"+CPK_twice+"⌟")
			traceback.print_exc()

		countCPK.close()
	# print('===Count CPK Done===')
	FulearnCur.close()
	
	with open('./Output.sql' ,'wb') as f:
		f.write(bytearray(''.join(SqlList),"utf-8"))
		f.close()
	#程式執行前先清空舊資料
	# truncate = commonObj.MySqlConn.cursor()
	# truncate.execute(textwrap.dedent('''
	# 	DELETE FROM label WHERE logic_type = 'analog'
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