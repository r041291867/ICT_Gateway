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
from decimal import * 

getcontext().prec = 15

class common() :
	MySqlConn = None
	GatewayName = 'AnalogPowered'

commonObj = common()

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
		commonObj.MySqlConn = pymysql.connect(host=config.get('MySQL','mysqlserver')
			,user=config.get('MySQL','mysqluser')
			,passwd=config.get('MySQL','mysqlpassword')
			,db=config.get('MySQL','database')
			,charset='utf8')
	except Exception as inst:
		print('MySql Connection Fail')
		print(inst)
		logging.error('{0} happen MySql Connection Fail'.format(commonObj.GatewayName))
		logging.error(inst)
	
def Fetch() :
	if commonObj.MySqlConn == None :
		print('No Db Conn')
		return None
	logging.info('{0} Start'.format(commonObj.GatewayName))
	print('{0} Start'.format(commonObj.GatewayName))
	stored_CPK = {}			#儲存已計算的CPK
	FulearnCur = commonObj.MySqlConn.cursor()
	#抓取fail資料
	FulearnCur.execute(textwrap.dedent('''
		SELECT a.*,b.`board` FROM `analog_powered_result` a 
		INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time AND a.status != 0 WHERE b.board='73-18275-04' 
		GROUP BY `sn`,`component`,`test_condition` ORDER BY `end_time` ASC
		'''))
	SqlList = []
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
		sfc_repair = 0
		label = 'NULL'
		isDone = False			#邏輯判斷結束
		#查找是否重測
		Retest_Pass = False
		# print ('find re-test ' + sn + ' ' + component + ' ' + test_condition)
		findRetest = commonObj.MySqlConn.cursor()
		findRetest.execute(textwrap.dedent('''
			SELECT a.*,b.`board` FROM `analog_powered_result` a
			INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
			WHERE b.board='73-18275-04' AND a.`sn` = '{0}' AND a.`component` = '{1}' AND a.`test_condition` = '{2}' AND a.end_time > '{3}'
			ORDER BY `end_time` ASC LIMIT 1
			'''.format(sn,component,test_condition,end_time)))
		isDone = False		#邏輯判斷結束
		re_sn = ''
		re_time = ''
		re_test_condition = ''
		if findRetest.rowcount == 0 :   #沒有重測 or SQL query錯誤
			label = '找不到重測紀錄'
		else :			#重測有資料
			for line in findRetest :
				#查找重測是否成功
				re_sn = line[1]
				re_test_condition = line[6]
				re_status = line[2]    #block_status
				re_time = line[11]
				if re_status == '00' : 
					Retest_Pass = True
			if Retest_Pass is True:
				#計算CPK
				CPK = 0
				s = component+'|'+test_condition
				if s in stored_CPK:
					CPK = stored_CPK[s]
					CPKK = commonObj.MySqlConn.cursor()
					CPKK.execute(textwrap.dedent('''
						UPDATE ICT_Project.analog_powered_result a
						INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
						SET a.cpk = '{0}' WHERE b.board='73-18275-04' AND a.component = '{1}' AND a.test_condition = '{2}';
						'''.format(CPK,component,test_condition)))
					commonObj.MySqlConn.commit()
					if CPK > 0.67 : label = '探針或測試點接觸問題(' + str(CPK) + ')' 
					else : label = '程式不穩定(' + str(CPK) + ')'
				else:
					print('===Count CPK===')
					countCPK = commonObj.MySqlConn.cursor()
					countCPK.execute(textwrap.dedent('''
						SELECT * FROM `analog_powered_result` a
						INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
						WHERE b.board='73-18275-04' AND a.component = '{0}' AND a.test_condition = '{1}' ORDER BY a.`end_time` ASC
						'''.format(component,test_condition)))
					T = []
					nominal = 0
					HighAndLow = []
					total = []
					for data in countCPK:
						measured_2 = data[5]
						nominal_2 = data[8]
						high_limit_2 = data[9]
						low_limit_2 = data[10]
						if (measured_2 >= 0 and measured_2 <= ((high_limit_2+low_limit_2)/2)*50):		#篩選掉明顯有問題的資料
							if (high_limit_2-low_limit_2) != 0:
								T.append(high_limit_2-low_limit_2)
							HighAndLow.append(high_limit_2+low_limit_2)
							nominal = nominal_2
							total.append(measured_2)
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
					stored_CPK[s] = CPK
					print('CPK = ' + str(CPK) + '\n')
					CPKK = commonObj.MySqlConn.cursor()
					CPKK.execute(textwrap.dedent('''
						UPDATE ICT_Project.analog_powered_result a
						INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
						SET a.cpk = '{0}' WHERE b.board='73-18275-04' AND a.component = '{1}' AND a.test_condition = '{2}';
						'''.format(CPK,component,test_condition)))
					commonObj.MySqlConn.commit()
					CPKK.close()
					if CPK > 0.67 : 
						label = '探針或測試點接觸問題'
					else : label = '程式或治具問題'
					countCPK.close()
			else: 
				#SFC查找紀錄
				SFC_result=[]
				has_record=False 	#是否有維修紀錄
				Retest_Pass = False	#重測是否通過
				isNDF = False 		#是否NPF
				try:
					#往前抓１天 往後抓７天
					delta1 = datetime.timedelta(days=1)
					delta7 = datetime.timedelta(days=7)
					startTime = str(end_time - delta1)[:10]
					endTime = str(end_time + delta7)[:10]
					BU = 'UAG'
					# print('http://10.157.20.101:8082/Api/repair?startTime='+startTime+'&endTime='+endTime+'&BU='+BU)
					r = requests.get('http://10.157.20.101:8082/Api/repair?startTime='+startTime+'&endTime='+endTime+'&BU='+BU)
					SFC_result = r.json() 
				except Exception as err:
					print('!!!!'+str(err)+'!!!!')
				try:
					for repair_info in SFC_result['data'] :
						if repair_info[',repair:']['Sysserailno'] == sn :
							has_record = True
							sfc_repair = 1
							if repair_info[',repair:']['FailureCode'] != 'NDF':
								isNDF = False
							else: isNDF = True
				except Exception as err:
					print('!!!!'+str(err)+'!!!!')
				if has_record is False :
					label = '無維修紀錄'
					# noRecord_Day += 1
				elif isNDF is True: 
					label = 'NPF'
					# isNDF_Day += 1 
				else:
					#查找是否重測(第二次)
					repair_but_failed = False
					findRetest_again = commonObj.MySqlConn.cursor()
					findRetest_again.execute(textwrap.dedent('''
						SELECT a.*,b.`board` FROM `analog_powered_result` a
						INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
						WHERE b.board='73-18275-04' AND a.`sn` = '{0}' AND a.`component` = '{1}' AND a.`test_condition` = '{2}' AND a.`end_time` > '{3}'
						ORDER BY `end_time` ASC LIMIT 1
						'''.format(re_sn,component,re_test_condition,re_time)))
					if findRetest_again.rowcount == 0 :   #沒有重測 or SQL query錯誤
						label = '有維修紀錄但無重測紀錄'
						isDone = True
						# print('find RetestAgain Failed')
					else:
						for line_again in findRetest_again :
							if line_again[2] == '00' : 
								Retest_Pass = True
						if Retest_Pass is True :
							label = '零件或製程問題'
						else:
							label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗'
		findRetest.close()

		SqlList.append(textwrap.dedent('''
			UPDATE ICT_Project.analog_powered_result AS a 
			INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
			SET a.sfc_repair = '{0}',a.label = '{1}' WHERE b.board='73-18275-04' AND a.sn = '{2}' AND a.component = '{3}' AND a.test_condition = '{4}'
			'''.format(sfc_repair,label,sn,component,test_condition)))
	with open('./Output.sql' ,'wb') as f:
		f.write(bytearray(''.join(SqlList),"utf-8"))
		f.close()
		
	FulearnCur.close()
	
	Cur = commonObj.MySqlConn.cursor()

	for update in SqlList:
		Cur.execute(update)
		commonObj.MySqlConn.commit()
	Cur.close()

	commonObj.MySqlConn.close()
	logging.info('{0} Finish'.format(commonObj.GatewayName))
	print('{0} Finish'.format(commonObj.GatewayName))
	
aStart = time.time()
main()
Fetch()
aEnd = time.time()
print ("===== All cost %f sec =====" % (aEnd - aStart))