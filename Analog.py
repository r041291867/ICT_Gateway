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
	GatewayName = 'Analog Fail Check'

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
	aStart = time.time()#計時開始
	if commonObj.MySqlConn == None :
		print('No Db Conn')
		return None
	logging.info('{0} Start'.format(commonObj.GatewayName))
	print('{0} Start'.format(commonObj.GatewayName))
	stored_sn = []			#儲存有問題的sn
	stored_component = []	#儲存已計算的零件
	stored_CPK = {}			#儲存已計算的CPK
	FulearnCur = commonObj.MySqlConn.cursor()
	#抓取fail資料
	FulearnCur.execute(textwrap.dedent('''
		SELECT `machine`,`sn`,`block_status`,`component`,`test_type`,`status`,`end_time`,`seq` FROM `analog_result_18275`
		WHERE status = 1 GROUP BY `sn`,`component`,`test_type` ORDER BY `end_time` ASC, `seq` ASC
		'''))
	SqlList = []
	# print (FulearnCur.rowcount)
	for row in FulearnCur :
		machine = row[0]
		sn = row[1]
		block_status = row[2]
		component = row[3]
		test_type = row[4]
		status = row[5]	
		# measured = row[6]
		# test_condition = row[7]
		# limit_type = row[8]
		# nominal = row[9]
		# high_limit = row[10]
		# low_limit = row[11]
		end_time = row[6]
		seq = row[7]
		sfc_repair = 0
		label = 'NULL'
		isDone = False			#邏輯判斷結束
		#查找是否重測
		Retest_Pass = False
		print ('find re-test ' + sn + ' ' + component)
		zstart = time.time()
		findRetest = commonObj.MySqlConn.cursor()
		findRetest.execute(textwrap.dedent('''
			SELECT * FROM `analog_result_18275` WHERE `sn` = '{0}' AND `component` = '{1}' AND end_time = '{2}' AND seq > '{3}' AND test_type = '{4}' 
			ORDER BY `seq` ASC
			'''.format(sn,component,end_time,seq,test_type)))
		zend = time.time()
		print('======retest use %f sec =====' % (zend - zstart))
		isDone = False		#邏輯判斷結束
		re_sn = ''
		re_time = ''
		if findRetest.rowcount == 0 :   #沒有重測 or SQL query錯誤
			label = '找不到重測紀錄'
		else :			#重測有資料
			for line in findRetest :
				#查找重測是否成功
				re_sn = line[1]
				re_status = line[2]    #block_status
				re_component = line[3]
				re_time = line[12]
				no_ShareBRC = False
				program_unstable = False
				if re_status == '00' : 
					Retest_Pass = True
			if Retest_Pass is True:
				#找出該零件的針點
				WireList = commonObj.MySqlConn.cursor()
				WireList.execute(textwrap.dedent('''
					SELECT * FROM `wirelist` WHERE `board` = '73-18275-04' AND `component` = '{0}'
					'''.format(re_component)))
				sharedBRC = []			#儲存針點的零件以便查詢共用針點的sn
				#找出針點共用零件
				for wire in WireList :
					wire_component = wire[2]
					wire_BRC = wire[5]
					ShareBRC = commonObj.MySqlConn.cursor()
					ShareBRC.execute(textwrap.dedent('''
						SELECT * FROM `wirelist` WHERE `board` = '73-18275-04' AND `BRC` = '{0}' AND component != '{1}'
						'''.format(wire_BRC,wire_component)))
					if ShareBRC.rowcount == 0 : 
						#找不到共用針點則直接挑出
						no_ShareBRC = True		#沒有共用針點
						break
					else:
						for other_wire in ShareBRC:
							other_component = other_wire[2]
							#儲存零件
							sharedBRC.append(other_component) 
					ShareBRC.close()
				#使用個別零件尋找其他sn
				if no_ShareBRC is False:
					for BRC in sharedBRC:
						findSN = commonObj.MySqlConn.cursor()
						findSN.execute(textwrap.dedent('''
							SELECT `block_status` FROM `analog_result_18275`
							where component = '{0}'
							ORDER BY `end_time` ASC, `seq` ASC
							'''.format(BRC)))
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
									break
						if program_unstable is True: 
							break
						else :
							stored_sn.append(sn)
							label = '探針或測試點接觸問題'
						findSN.close()
				if no_ShareBRC is True :
					#計算CPK
					CPK = 0
					if component in stored_CPK:
						CPK = stored_CPK[component]
						if CPK > 0.67 : label = '探針或測試點接觸問題(' + str(CPK) + ')' 
						else : label = '程式不穩定(' + str(CPK) + ')'
					else:
						print('===Count CPK===')
						# t1 = time.time()
						stored_component.append(component+'|'+test_type)
						countCPK = commonObj.MySqlConn.cursor()
						countCPK.execute(textwrap.dedent('''
							SELECT * FROM `analog_result_18275`
							WHERE component = '{0}' AND test_type = '{1}' ORDER BY `end_time` ASC
							'''.format(re_component,test_type)))
						# t2 = time.time()
						# print('======find cpk use %f sec =====' % (t2 - t1))
						T = []
						nominal = 0
						HighAndLow = []
						total = []
						for data in countCPK:
							if (data[6] >= 0 and data[6] <= ((data[10]+data[11])/2)*50):		#篩選掉明顯有問題的資料
								if (data[10]-data[11]) != 0:
									T.append(data[10]-data[11])
								HighAndLow.append(data[10]+data[11])
								nominal = data[9]
								total.append(data[6])
						MEAN = np.mean(total)
						VAR = np.std(total)
						if nominal is None : 
							nominal = HighAndLow[0]/2
						# if T[0] == 0 or T[0] is None :
						# 	break
						CA = abs((MEAN - nominal)/(T[0]/2))
						CP = T[0]/(VAR*6)
						CPK = (1-CA)*(CP)
						stored_CPK[component] = CPK
						isDone = True
						# t3 = time.time()
						# print('======count use %f sec =====' % (t3 - t2))
						print('CPK = ' + str(CPK) + '\n')
						if CPK > 0.67 : 
							stored_sn.append(sn)
							label = '探針或測試點接觸問題(' + str(CPK) + ')' 
						else : label = '程式不穩定(' + str(CPK) + ')'
						countCPK.close()
				WireList.close()
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
					print('http://10.157.20.101:8082/Api/repair?startTime='+startTime+'&endTime='+endTime+'&BU='+BU)
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
						SELECT * FROM `analog_result_18275` WHERE `sn` = '{0}' AND `component` = '{1}' AND end_time > '{2}' AND test_type = '{3}' 
						ORDER BY `end_time` ASC, `seq` ASC
						'''.format(re_sn,component,re_time,test_type)))
					if findRetest_again.rowcount == 0 :   #沒有重測 or SQL query錯誤
						label = '有維修紀錄但無重測紀錄'
						isDone = True
					else:
						for line_again in findRetest_again :
							if line_again[2] == '00' : 
								Retest_Pass = True
						if Retest_Pass is True :
							stored_sn.append(sn)
							label = '零件或製程問題'
						else:
							label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗'
		findRetest.close()
		#寫入資料表
		SqlList.append(textwrap.dedent('''
			UPDATE ICT_Project.analog_result SET sfc_repair = '{0}',label = '{1}' WHERE seq = '{2}';
			'''.format(sfc_repair,label,seq)))
		Cur = commonObj.MySqlConn.cursor()
		Cur.execute(textwrap.dedent('''
			UPDATE ICT_Project.analog_result_18275 SET sfc_repair = '{0}',label = '{1}' WHERE sn = '{2}' AND component = '{3}' AND test_type = '{4}';
			'''.format(sfc_repair,label,sn,component,test_type)))
		commonObj.MySqlConn.commit()
		Cur.close()
	with open('./Output.sql' ,'wb') as f:
		f.write(bytearray(''.join(SqlList),"utf-8"))
		f.close()
	stored_sn_new = list(set(stored_sn))
	stored_component_new = list(set(stored_component))
	for CPK_twice in stored_component_new:
		#計算第二次CPK
		print('===Count CPK Twice===')
		countCPK = commonObj.MySqlConn.cursor()
		sp = CPK_twice.split('|')
		countCPK.execute(textwrap.dedent('''
			SELECT * FROM `analog_result_18275`
			WHERE component = '{0}' AND test_type = '{1}' ORDER BY `end_time` ASC
			'''.format(sp[0],sp[1])))
		T = []
		nominal = 0
		HighAndLow = []
		total = []
		for data in countCPK:
			sn2 = data[1]
			measured2 = data[6]
			nominal2 = data[9]
			high_limit2 = data[10]
			low_limit2 = data[11]
			if sn2 not in stored_sn:
				if (measured2 >= 0 and measured2 <= ((high_limit2+low_limit2)/2)*5):		#篩選掉明顯有問題的資料
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
		print('CPK = ' + str(CPK) + '\n')
		Cur = commonObj.MySqlConn.cursor()
		Cur.execute(textwrap.dedent('''
			UPDATE ICT_Project.analog_result_18275 SET cpk = '{0}' WHERE component = '{1}' AND test_type = '{2}';
			'''.format(CPK,sp[0],sp[1])))
		commonObj.MySqlConn.commit()
		Cur.close()
		countCPK.close()
	FulearnCur.close()
	
	# Cur = commonObj.MySqlConn.cursor()

	# for update in SqlList:
	# 	Cur.execute(update)
	# 	commonObj.MySqlConn.commit()
	# Cur.close()
	aEnd = time.time()#計時結束
	print ("===== All cost %f sec =====" % (aEnd - aStart))
	commonObj.MySqlConn.close()
	logging.info('{0} Finish'.format(commonObj.GatewayName))
	print('{0} Finish'.format(commonObj.GatewayName))
	
	
main()
Fetch()