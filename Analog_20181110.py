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

	FulearnCur = commonObj.MySqlConn.cursor()
	#抓取fail資料
	print ('catch fail data')
	# FulearnCur.execute(textwrap.dedent('''
	# 	SELECT a.`machine`,a.`sn`,a.`block_status`,a.`component`,a.`test_type`,a.`status`,a.`end_time`,a.`seq`,b.`board` FROM `analog_result` a
	# 	inner join ict_result b on a.`machine`=b.`machine` and a.`sn`=b.`sn` and a.`end_time`=b.`end_time` AND a.`status` != 0 where b.`board` = '73-18275-04' 
	# 	GROUP BY a.`sn`,a.`component` ORDER BY a.`end_time` ASC, `a`.`seq` ASC
	# 	'''))
	FulearnCur.execute(textwrap.dedent('''
		SELECT `machine`,`sn`,`block_status`,`component`,`test_type`,`status`,`end_time`,`seq` FROM `analog_result_18275`
		WHERE status != 0 GROUP BY `sn`,`component` ORDER BY `end_time` ASC, `seq` ASC
		'''))

	for row in FulearnCur :
		tStart = time.time()#計時開始
		machine = row[0]
		sn = row[1]
		block_status = row[2]
		component = row[3]
		test_type = row[4]
		status = row[5]
		#measured = row[6]
		#test_condition = row[7]
		#limit_type = row[8]
		#nominal = row[9]
		#high_limit = row[10]
		#low_limit = row[11]
		end_time = row[6]
		seq = row[7]
		sfc_repair = 0
		label = ''
		SqlList = []
		isDone = False			#邏輯判斷結束
		repair_but_failed = False
		# noNPF_noPASS_Day = 1
		# noNPF_noPASS = False
		isNDF_Day = 1
		noRecord_Day = 1
		while True: #如果是NDF/沒有sfc紀錄則跳到這裡重測
			#查找是否重測
			if noRecord_Day == 7:
				isDone = True
				label = '無維修記錄'
				break
			if isNDF_Day == 7:
				isDone = True
				label = 'NPF'
				break
			# if noNPF_noPASS is False:
			print ('find re-test ' + sn + ' ' + component)
			findRetest = commonObj.MySqlConn.cursor()
			findRetest.execute(textwrap.dedent('''
				SELECT * FROM `analog_result_18275` WHERE `sn` = '{0}' AND `component` = '{1}' AND end_time > '{2}' ORDER BY `end_time` ASC, `seq` asc 
				'''.format(sn,component,end_time)))
			#print (findRetest.rowcount)
			isDone = False		#邏輯判斷結束
			re_sn = ''
			re_time = ''
			if findRetest.rowcount == 0 :   #沒有重測 or SQL query錯誤
				label = '資料不足'
				print('find Retest Failed')
				break
			for line in findRetest :		
				# if noNPF_noPASS is True : #7天都失敗則直接跳出
				# 	if noNPF_noPASS_Day == 7:
				# 		isDone = True
				# 		label = '資料有誤'
				# 	else: noNPF_noPASS_Day += 1
				# 	break
				#查找重測是否成功
				print('if re-test success?')
				re_sn = line[1]
				re_status = line[2]    #block_status
				re_component = line[3]
				re_time = line[12]
				no_ShareBRC = False
				program_unstable = False
				if re_status == '00' : 			#Pass
					#找出該零件的針點
					print ('find BRC')
					WireList = commonObj.MySqlConn.cursor()
					WireList.execute(textwrap.dedent('''
						SELECT * FROM `wirelist` WHERE `board` = '73-18275-04' AND `component` = '{0}'
						'''.format(re_component)))
					sharedBRC = []			#儲存針點的零件以便查詢共用針點的sn
					#找出針點共用零件
					for wire in WireList :
						print ('find sharedBRC')
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
						#儲存零件
						sharedBRC.append(wire_component) 

					#使用個別零件尋找其他sn
					for BRC in sharedBRC:
						print ('find sn')
						findSN = commonObj.MySqlConn.cursor()
						# findSN.execute(textwrap.dedent('''
						# 	SELECT a.`block_status`,b.`board` FROM `analog_result_18275` a 
						# 	inner join ict_result b on a.machine=b.machine and a.sn=b.sn and a.end_time=b.end_time AND a.status != 0 where b.board='73-18275-04' AND a.component = '{0}'
						# 	ORDER BY a.`end_time` ASC, `a`.`seq` ASC
						# 	'''.format(BRC)))
						findSN.execute(textwrap.dedent('''
							SELECT `block_status` FROM `analog_result_18275`
							where component = '{0}'
							ORDER BY `end_time` ASC, `seq` ASC
							'''.format(BRC)))
						if findSN.rowcount == 0:
							#有查到共用針點但是沒有測試結果
							no_ShareBRC = True
							break
						for findSN_result in findSN :
							#一次PASS則結束
							if findSN_result[0] == '00':
								program_unstable = True
								isDone = True
								label = '程式不穩定'
								break
						if program_unstable is True: break
					if program_unstable is False :
						isDone = True
						label = '探針或測試點接觸問題'

					if no_ShareBRC is True :
						#計算CPK
						print('Count CPK')
						countCPK = commonObj.MySqlConn.cursor()
						# countCPK.execute(textwrap.dedent('''
						# 	SELECT a.* FROM `analog_result` a
						# 	inner join ict_result b on a.`machine`=b.`machine` and a.`sn`=b.`sn` and a.`end_time`=b.`end_time` 
						# 	WHERE `board` = '73-18275-04' AND component = '{0}' ORDER BY a.`end_time` ASC
						# 	'''.format(re_component)))
						countCPK.execute(textwrap.dedent('''
							SELECT * FROM `analog_result_18275`
							WHERE component = '{0}' ORDER BY `end_time` ASC
							'''.format(re_component)))
						T = []
						nominal = 0
						HighAndLow = []
						total = []
						for data in countCPK:
							if (data[6] >= 0 and data[6] <= ((data[10]+data[11])/2)*50):		#篩選掉明顯有問題的資料
								T.append(data[10]-data[11])
								HighAndLow.append(data[10]+data[11])
								nominal = data[9]
								total.append(data[6])
						MEAN = np.mean(total)
						VAR = np.std(total)
						print(re_component)
						
						if nominal is None : 
							nominal = HighAndLow[0]/2
						if T[0] == 0 or T[0] is None :
							break
						CA = abs((MEAN - nominal)/(T[0]/2))
						CP = T[0]/(VAR*6)
						CPK = (1-CA)*(CP)
						isDone = True
						print('MEAN = ' + str(MEAN))
						print('nominal = ' + str(nominal))
						print('T = ' + str(T[0]))
						print('CA = ' + str(CA))
						print('CP = ' + str(CP))
						print('CPK = ' + str(CPK))
						if CPK > 0.67 : label = '探針或測試點接觸問題(' + str(CPK) + ')' 
						else : label = '程式不穩定(' + str(CPK) + ')'
						countCPK.close()
					WireList.close()
			# else:
				# if noNPF_noPASS_Day == 7:
					# isDone = True
					# label = '資料有誤'
				# else: noNPF_noPASS_Day += 1
			if isDone is True: break
			#SFC查找紀錄
			countRepairDay = 1		#計算天數 超過7天則直接跳出
			while True:		#沒有維修紀錄則24小時後再來查詢
				print ('find sfc record')
				if countRepairDay == 7 :
					isDone = True
					sfc_repair = 0
					label = '無維修紀錄'
					break
				countRepairDay += 1
				SFC_result=[]
				has_record=False 	#是否有維修紀錄
				Retest_Pass = False	#重測是否通過
				isNDF = False 		#是否NPF
				try:
					#日期格式轉換
					#Etime = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")  #error
					#往前抓１天 往後抓７天
					delta1 = datetime.timedelta(days=1)
					delta7 = datetime.timedelta(days=7)
					startTime = str(end_time - delta1)[:10]
					endTime = str(end_time + delta7)[:10]
					BU = 'UAG'
					r = requests.get('http://10.157.20.101:8082/Api/repair?startTime='+startTime+'&endTime='+endTime+'&BU='+BU)
					SFC_result = r.json() 
				except Exception as err:
					print('!!!!'+str(err)+'!!!!')
				if data in SFC_result:
					for repair_info in SFC_result['data'] :
						if repair_info[',repair:']['Sysserailno'] == sn :
							has_record = True
							sfc_repair = 1
							if repair_info[',repair:']['FailureCode'] != 'NDF':
								isNDF = False
							else: isNDF = True
						# else:
						# 	sfc_repair = 0 
						# 	has_record = False
						# 	noRecord_Day += 1
				else:
					print('===API Error===')
					label = 'API錯誤'
					isDone = True
					break
				if has_record is False :
					noRecord_Day += 1
				elif isNDF is True: 
					isNDF_Day += 1 
					break
				else:
					#查找是否重測
					print ('re-test again')
					findRetest_again = commonObj.MySqlConn.cursor()
					findRetest_again.execute(textwrap.dedent('''
						SELECT * FROM `analog_result_18275` WHERE `sn` = '{0}'  AND `component` = '{1}' AND  `end_time` > '{2}' 
						'''.format(re_sn,component,re_time)))
					if findRetest_again.rowcount == 0 :   #沒有重測 or SQL query錯誤
						label = '有維修紀錄但無重測紀錄'
						isDone = True
						print('find RetestAgain Failed')
						break
					for line_again in findRetest_again :
						# re_time =  line_again[11]
						if line_again[2] == '00' : 	#PASS
							Retest_Pass = True
							label = '零件或製程問題'
							isDone = True
							break
						else: 
							noNPF_noPASS = True	    
					if noNPF_noPASS is True : break	
				#else: 
					#等待24小時之後繼續執行	    				
					#time.sleep(86400)
				#if has_record == True : break	
				# if repair_but_failed == True : break
				if has_record == True : break	
				if isDone is True : break	
			if isDone is True : break	
			# label = '零件或製程問題'
			findRetest.close()
		tEnd = time.time()#計時結束
		print ("=== It cost %f sec ===" % (tEnd - tStart))
		#寫入資料表
		SqlList.append(textwrap.dedent('''
			UPDATE ICT_Project.analog_result SET sfc_repair = '{0}',label = '{1}' WHERE seq = '{2}';
			'''.format(sfc_repair,label,seq)))
		Cur = commonObj.MySqlConn.cursor()
		Cur.execute(textwrap.dedent('''
			UPDATE ICT_Project.analog_result_18275 SET sfc_repair = '{0}',label = '{1}' WHERE seq = '{2}';
			'''.format(sfc_repair,label,seq)))
		commonObj.MySqlConn.commit()
		Cur.close()
	with open('./Output.sql' ,'wb') as f:
		f.write(bytearray(''.join(SqlList),"utf-8"))
		f.close()
		
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