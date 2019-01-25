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

getcontext().prec = 15

class common() :
	MySqlConn = None
	GatewayName = 'Analog Fail Check'

commonObj = common()
# 維修代碼
ErrCode = {
	'E101': 'not NDF', 'E102': 'not NDF', 'E103': 'not NDF', 'E105': 'not NDF', 'E106': 'not NDF', 
	'E201': 'not NDF', 'E202': 'not NDF', 'E203': 'not NDF', 'E204': 'not NDF', 'E205': 'not NDF', 
	'E206': 'not NDF', 'E208': 'not NDF', 'E209': 'not NDF', 'E210': 'not NDF', 'E211': 'not NDF', 
	'E212': 'not NDF', 'E213': 'not NDF', 'E214': 'not NDF', 'E215': 'not NDF', 'E216': 'not NDF', 
	'E217': 'not NDF', 'E218': 'not NDF', 'E219': 'not NDF', 'E220': 'not NDF', 'E221': 'not NDF', 
	'E222': 'not NDF', 'E223': 'not NDF', 'E224': 'not NDF', 'E301': 'not NDF', 'E302': 'not NDF', 
	'E303': 'not NDF', 'E304': 'not NDF', 'E305': 'not NDF', 'E306': 'not NDF', 'E307': 'not NDF', 
	'E308': 'not NDF', 'E309': 'not NDF', 'E310': 'not NDF', 'E311': 'not NDF', 'E312': 'not NDF', 
	'E313': 'not NDF', 'E314': 'not NDF', 'E315': 'not NDF', 'E316': 'not NDF', 'E317': 'not NDF', 
	'E318': 'not NDF', 'E319': 'not NDF', 'E320': 'not NDF', 'E401': 'not NDF', 'E402': 'not NDF', 
	'E403': 'not NDF', 'E405': 'not NDF', 'E406': 'not NDF', 'E407': 'not NDF', 'E408': 'not NDF', 
	'E501': 'not NDF', 'E502': 'not NDF', 'E503': 'not NDF', 'E504': 'not NDF', 'E505': 'not NDF', 
	'E506': 'not NDF', 'E507': 'not NDF', 'E508': 'not NDF', 'E509': 'not NDF', 'E510': 'not NDF', 
	'E511': 'not NDF', 'E512': 'not NDF', 'E513': 'not NDF', 'E518': 'not NDF', 'E702': 'not NDF', 
	'E703': 'not NDF', 'E704': 'not NDF', 'E728': 'not NDF', 'E741': 'not NDF', 'E742': 'not NDF', 
	'E743': 'not NDF', 'E903': 'not NDF', 'E905': 'not NDF', 'E907': 'not NDF', 'E744': 'not NDF', 
	'E970': 'not NDF', 'E971': 'not NDF', 'E972': 'not NDF', 'E973': 'not NDF', 'E974': 'not NDF', 
	'E975': 'NDF', 'E976': 'NDF', 'E108': 'not NDF', 'E107': 'not NDF', 'E845': 'not NDF', 
	'E011': 'NDF', 'E977': 'NDF', 'E514': 'not NDF', 'E515': 'not NDF', 'E516': 'not NDF', 
	'E517': 'not NDF', 'E718': 'not NDF', 'E519': 'not NDF', 'E520': 'not NDF', 'E521': 'not NDF', 
	'E522': 'not NDF', 'E523': 'not NDF', 'E601': 'not NDF', 'E602': 'not NDF', 'E603': 'not NDF', 
	'E604': 'not NDF', 'E701': 'not NDF', 'E045': 'not NDF', 'E705': 'not NDF', 'E706': 'not NDF', 
	'E707': 'not NDF', 'E708': 'not NDF', 'E709': 'not NDF', 'E710': 'not NDF', 'E711': 'not NDF', 
	'E712': 'not NDF', 'E714': 'not NDF', 'E715': 'not NDF', 'E716': 'not NDF', 'E717': 'not NDF', 
	'E719': 'not NDF', 'E720': 'not NDF', 'E721': 'not NDF', 'E722': 'not NDF', 'E723': 'not NDF', 
	'E725': 'not NDF', 'E726': 'not NDF', 'E729': 'not NDF', 'E730': 'not NDF', 'E731': 'not NDF', 
	'E732': 'not NDF', 'E733': 'not NDF', 'E734': 'not NDF', 'E738': 'not NDF', 'E739': 'not NDF', 
	'E740': 'not NDF', 'E801': 'not NDF', 'E806': 'NDF', 'E807': 'NDF', 'E808': 'NDF', 
	'E809': 'NDF', 'E810': 'NDF', 'E812': 'NDF', 'E813': 'NDF', 'E814': 'NDF', 
	'E819': 'not NDF', 'E820': 'not NDF', 'E822': 'not NDF', 'E824': 'not NDF', 'E825': 'not NDF', 
	'E836': 'not NDF', 'E837': 'not NDF', 'E840': 'not NDF', 'E841': 'not NDF', 'E901': 'not NDF', 
	'E981': 'not NDF', 'E982': 'not NDF', 'E904': 'not NDF', 'E983': 'not NDF', 'E906': 'NDF', 
	'E984': 'not NDF', 'E908': 'not NDF', 'E909': 'not NDF', 'E910': 'not NDF', 'E911': 'not NDF', 
	'E912': 'not NDF', 'E913': 'not NDF', 'E914': 'not NDF', 'E985': 'not NDF', 'E916': 'not NDF', 
	'E917': 'not NDF', 'E918': 'not NDF', 'E919': 'not NDF', 'E986': 'not NDF', 'E987': 'NDF', 
}

# 根據下的參數轉換執行環境
Env = {}
Env['ICT'] = ['ICT','analog_result_18275','73-18275-04','label_18275']
Env['ICT4'] = ['ICT','analog_result_18274','73-18274-04','label_18274']
Env['ICTs'] = ['ICT','analog_18275_1215','73-18275-04','label_18275_1215']
Env['ICT_Exp'] = ['ICT_exp','analog_result','73-18275-04','label_18275']
TestDB = ''
TestTB = ''
TestBoard = ''
if len(sys.argv) > 1 :
	TestDB = Env[sys.argv[1]][0]
	TestTB = Env[sys.argv[1]][1]
	TestBoard = Env[sys.argv[1]][2]
	LabelTB = Env[sys.argv[1]][3]
else : 
	#未輸入參數的預設環境
	TestDB = 'ICT'
	TestTB = 'analog_result_18275'
	TestBoard = '73-18275-04'
	LabelTB = 'label_18275'

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
		commonObj.MySqlConn = pymysql.connect(host=config.get(TestDB,'mysqlserver')
			,user=config.get(TestDB,'mysqluser')
			,passwd=config.get(TestDB,'mysqlpassword')
			,db=config.get(TestDB,'database')
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
	print(TestDB+' '+TestTB+' '+TestBoard)
	stored_sn = []			#儲存有問題的sn
	stored_component = []	#儲存已計算的零件
	stored_CPK = {}			#儲存已計算的CPK
	FulearnCur = commonObj.MySqlConn.cursor()
	#抓取fail資料(測試步驟Fail)
	FulearnCur.execute(textwrap.dedent('''
		SELECT `machine`,`sn`,`block_status`,`component`,`test_type`,`status`,test_condition,`end_time`,`seq` FROM {0}
		WHERE status = 1 GROUP BY `sn`,`component`,`test_type`,test_condition ORDER BY `end_time` ASC, `seq` ASC
		'''.format(TestTB)))
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
		sfc_repair = 0
		label = '？？？'
		label_no = 999			#label編號: 0-無維修紀錄 1-零件或製程問題 2-程式不穩定 3-探針或接觸問題 4-零件與維修記錄無法匹配 5-找不到重測紀錄 6-wirelist查無資料 7-重測失敗
		isDone = False			#邏輯判斷結束
		isMatch = False			#FailSymptom是否一致
		isNDF = False 			#是否NPF
		debugRow = sn +' '+ component +' '+ test_type + str(end_time) + ': '			#追蹤流程走向
		day90 = datetime.timedelta(days=90) 	#90天前的紀錄不予理會
		min5 = datetime.timedelta(minutes=5) 	#匹配api資料內和資料庫的時間差（相差5分內的極大可能為同一資料）
		min1 = datetime.timedelta(minutes=1)
		now = datetime.datetime.now()		 	#獲取當前時間
		if end_time > (now - day90):
			debugRow = debugRow + 'in90d '+str(now)+' -> '
			#查詢SFC是否有fail紀錄
			retries = 0			#連接api時失敗重試
			success = False
			while retries < 7 and not success:
				try:
					BU = 'UAG'
					r = requests.get('http://10.157.20.101:8083/Api/fail?sn='+sn+'&BU='+BU)
					if r.status_code == requests.codes.ok : success = True
					SFC_fail = r.json() 
				except Exception as err:
					retries += 1
					print(r.raise_for_status()) 
					if retries == 7 : break
			sameSymptom = False
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
				has_record=False 	#是否有維修紀錄
				Retest_Pass = False	#重測是否通過
				isMatch = True
				retries = 0			#連接api時失敗重試
				success = False
				SFC_result = {}
				while retries < 7 and not success:
					try:
						BU = 'UAG'
						# print('http://10.157.20.101:8083/Api/repair?sn='+sn+'&BU='+BU)
						r = requests.get('http://10.157.20.101:8083/Api/repair?sn='+sn+'&BU='+BU)
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
				debugRow = debugRow + 'no match Symptom -> '
				#找不到fail紀錄 or FailSymptom不一致
				
			#找不到fail紀錄 or FailSymptom不一致 or NPF
			if sameSymptom is False or isNDF is True:
				debugRow = debugRow + 'find re-test -> '
				#查找是否重測
				Retest_Pass = False
				findRetest = commonObj.MySqlConn.cursor()
				findRetest.execute(textwrap.dedent('''
					SELECT * FROM {0} WHERE `sn` = '{1}' AND `component` = '{2}' AND test_type = '{3}' AND end_time >= '{4}'
					ORDER BY `seq` ASC
					'''.format(TestTB,sn,component,test_type,end_time)))			
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
							'''.format(TestBoard,re_component)))
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
									'''.format(TestBoard,BRC,component)))
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
									'''.format(TestBoard,sharedBRC[0],component,sharedBRC[1])))
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
										SELECT `block_status` FROM {0}
										where component = '{1}' and sn = '{2}'
										ORDER BY `end_time` ASC, `seq` ASC
										'''.format(TestTB,BRC,sn)))
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
							component_combine = component+'|'+test_type+'|'+test_condition
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
									SELECT * FROM {0}
									WHERE component = '{1}' AND test_type = '{2}' AND test_condition = '{3}' AND end_time > '{4}' 
									ORDER BY `end_time` ASC
									'''.format(TestTB,re_component,test_type,test_condition,(now - day90).strftime("%Y-%m-%d %H:%M:%S"))))
								# t2 = time.time()
								# print('======find cpk use %f sec =====' % (t2 - t1))
								T = []
								nominal = 0
								HighAndLow = []
								total = []
								for data in countCPK:
									if (abs(data[6]) <= abs(data[10]-data[11])*5):		#篩選掉明顯有問題的資料
										if (data[10]-data[11]) != 0:
											T.append(data[10]-data[11])
										HighAndLow.append(data[10]+data[11])
										nominal = data[9]
										total.append(data[6])
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
						WireList.close()
					else: 
						debugRow = debugRow + 're-test fail -> '
						label = "重測失敗"
						label_no = 7
						# print(label)
						# retest_fail += 1
				findRetest.close()
			#寫入資料表
			# SqlList.append(textwrap.dedent('''
			# 	UPDATE {0} SET sfc_repair = '{1}',label = '{2}' WHERE sn = '{3}' AND component = '{4}' AND test_type = '{5}' AND end_time = '{6}';
			# 	'''.format(TestTB,sfc_repair,label,sn,component,test_type,end_time)))
			SqlList.append(textwrap.dedent('''
				INSERT IGNORE INTO {0} (logic_type,seq,sn,component,test_type,test_condition,label,label_no) VALUES ('analog','{1}','{2}','{3}','{4}','{5}','{6}','{7}');
				'''.format(LabelTB,seq,sn,component,test_type,test_condition,label,label_no)))
		debugRow = debugRow + 'done\n'
		debug.append(debugRow)
		# Cur = commonObj.MySqlConn.cursor()
		# Cur.execute(textwrap.dedent('''
		# 	UPDATE analog_result_18275 SET sfc_repair = '{0}',label = '{1}' WHERE sn = '{2}' AND component = '{3}' AND test_type = '{4}';
		# 	'''.format(sfc_repair,label,sn,component,test_type)))
		# commonObj.MySqlConn.commit()
		# Cur.close()
	with open('./Seqence.txt' ,'wb') as fo:
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
			SELECT * FROM {0}
			WHERE component = '{1}' AND test_type = '{2}' AND test_condition = '{3}' AND end_time > '{4}'
			ORDER BY `end_time` ASC
			'''.format(TestTB,sp[0],sp[1],sp[2],(now - day90).strftime("%Y-%m-%d %H:%M:%S"))))
		T = []
		nominal = 0
		HighAndLow = []
		total = []
		try:
			for data in countCPK:
				sn2 = data[1]
				measured2 = data[6]
				nominal2 = data[9]
				high_limit2 = data[10]
				low_limit2 = data[11]
				if sn2 not in stored_sn:
					if (abs(measured2) <= abs(high_limit2-low_limit2)*5):		#篩選掉明顯有問題的資料
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
		# print('CPK = ' + str(CPK) + '\n')
		# SqlList.append(textwrap.dedent('''
		# 	UPDATE {0} SET cpk = '{1}' WHERE component = '{2}' AND test_type = '{3}';
		# 	'''.format(TestTB,CPK,sp[0],sp[1])))
			SqlList.append(textwrap.dedent('''
				UPDATE IGNORE {0} SET cpk = '{1}' WHERE component = '{2}' AND test_type = '{3}' AND test_condition = '{4}';
				'''.format(LabelTB,CPK,sp[0],sp[1],sp[2])))
		except Exception as err:
			print(r.raise_for_status()) 

		countCPK.close()
	# print('===Count CPK Done===')
	FulearnCur.close()
	
	with open('./Output.sql' ,'wb') as f:
		f.write(bytearray(''.join(SqlList),"utf-8"))
		f.close()
	#程式執行前先清空舊資料
	truncate = commonObj.MySqlConn.cursor()
	# truncate.execute(textwrap.dedent('''
	# 	TRUNCATE TABLE {0}
	# 	'''.format(LabelTB)))
	truncate.execute(textwrap.dedent('''
		DELETE FROM {0} WHERE logic_type = 'analog'
		'''.format(LabelTB)))
	truncate.close()

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