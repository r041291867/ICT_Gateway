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
	GatewayName = 'Short Fail Check'

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
	'E915': 'not NDF'
}

# 根據下的參數轉換執行環境
Env = {}
Env['ICT'] = ['ICT','open_short_result','73-18275-04','label_18275']
Env['ICT4'] = ['ICT','open_short_result','73-18274-04','label_18274']
Env['ICT_Exp'] = ['ICT_exp','open_short_result','73-18275-04','label_18275']
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
	TestTB = 'open_short_result'
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
		SELECT a.*,b.`board` FROM {0} a 
		INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time AND a.status != 0 WHERE b.board='{1}' 
		GROUP BY `sn` ORDER BY `end_time` ASC
		'''.format(TestTB,TestBoard)))
	SqlList = []
	debug = []
	# print (FulearnCur.rowcount)
	for row in FulearnCur :
		machine = row[0]
		sn = row[1]
		status = row[2]
		end_time = row[3]
		seq = row[4]
		sfc_repair = 0
		label = '？？？'
		label_no = 999			#label編號: 0-無維修紀錄 1-零件或製程問題 2-程式不穩定 3-探針或接觸問題 4-零件與維修記錄無法匹配 5-找不到重測紀錄 6-wirelist查無資料 7-重測失敗
		isDone = False			#邏輯判斷結束
		isMatch = False			#FailSymptom是否一致
		isNDF = False 			#是否NPF
		debugRow = sn +': '			#追蹤流程走向
		day90 = datetime.timedelta(days=90) 	#90天前的紀錄不予理會
		min5 = datetime.timedelta(minutes=5) 	#匹配api資料內和資料庫的時間差（相差5分內的極大可能為同一資料）
		min1 = datetime.timedelta(minutes=1)
		now = datetime.datetime.now()  	#獲取當前時間
		if end_time > (now - day90):
			debugRow = debugRow + 'in90d -> '
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
				if fail_info['Repair']['FailSymptom'] == 'failed shorts test' \
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
						print('http://10.157.20.101:8083/Api/repair?sn='+sn+'&BU='+BU)
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
							print ('failurecode: ' + failurecode + ' -> ' + ErrCode[failurecode])

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
				
			#找不到fail紀錄 or FailSymptom不一致 or NPF
			if sameSymptom is False or isNDF is True:
				debugRow = debugRow + 'find re-test -> '
				#查找是否重測
				Retest_Pass = False
				print ('find re-test ' + sn)
				zstart = time.time()
				findRetest = commonObj.MySqlConn.cursor()
				findRetest.execute(textwrap.dedent('''
					SELECT a.*,b.board FROM {0} a
					INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time
					WHERE b.board='{1}' AND a.sn = '{2}' AND a.end_time >= '{3}' 
					ORDER BY `seq` ASC 
					'''.format(TestTB,TestBoard,sn,end_time)))
				zend = time.time()
				print('======retest use %f sec =====' % (zend - zstart))
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
						re_status = line[2]    #block_status
						re_end_time = line[3]
						re_seq = line[4]
						no_ShareBRC = False
						program_unstable = False
						if re_status == '00' : 
							Retest_Pass = True
					if Retest_Pass is True:
						label = "程式或治具問題"
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
				INSERT IGNORE INTO {0} (logic_type,seq,sn,label,label_no) VALUES ('short','{1}','{2}','{3}','{4}');
				'''.format(LabelTB,seq,sn,label,label_no)))
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
	truncate = commonObj.MySqlConn.cursor()
	# truncate.execute(textwrap.dedent('''
	# 	TRUNCATE TABLE {0}
	# 	'''.format(LabelTB)))
	truncate.execute(textwrap.dedent('''
		DELETE FROM {0} WHERE logic_type = 'short'
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