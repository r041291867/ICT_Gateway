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
	GatewayName = 'PowerCheck'

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
		SELECT a.*,b.`board` FROM `power_on_result` a 
		INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time AND a.status != 0 WHERE b.board='73-18275-04' 
		GROUP BY `sn`,`power_check_type` ORDER BY `end_time` ASC
		'''))
	SqlList = []
	# print (FulearnCur.rowcount)
	for row in FulearnCur :
		machine = row[0]
		sn = row[1]
		power_check_type = row[2]
		block_status = row[3]
		status = row[4]
		measured = row[5]
		power_check = row[6]
		limit_type = row[7]
		nominal = row[8]
		high_limit = row[9]
		low_limit = row[10]
		end_time = row[11]
		seq = row[12]
		sfc_repair = 0
		CPK = 0
		label = 'NULL'
		isDone = False			#邏輯判斷結束
		#查找是否重測
		Retest_Pass = False
		# print ('find re-test ' + sn)
		findRetest = commonObj.MySqlConn.cursor()
		findRetest.execute(textwrap.dedent('''
			SELECT a.*,b.`board` FROM `power_on_result` a
			INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
			WHERE b.board='73-18275-04' AND a.`sn` = '{0}' AND a.`end_time` > '{1}' AND a.`power_check_type` = '{2}'
			GROUP BY `end_time` ORDER BY `end_time` ASC LIMIT 1
			'''.format(sn,end_time,power_check_type)))
		isDone = False		#邏輯判斷結束
		re_sn = ''
		re_time = ''
		re_pwr_type = ''
		if findRetest.rowcount == 0 :   #沒有重測 or SQL query錯誤
			label = '找不到重測紀錄'
		else :			#重測有資料
			for line in findRetest :
				#查找重測是否成功
				re_sn = line[1]
				re_pwr_type = line[2]
				re_status = line[3]    #block_status
				re_time = line[11]
				if re_status == '00' : 
					Retest_Pass = True
			if Retest_Pass is True:
				#計算CPK
				CPK = 0
				if power_check in stored_CPK:
					CPK = stored_CPK[power_check]
				else:
					print('===Count CPK===')
					# t1 = time.time()
					countCPK = commonObj.MySqlConn.cursor()
					countCPK.execute(textwrap.dedent('''
						SELECT a.* FROM `power_on_result` a 
						INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
						WHERE b.board='73-18275-04' AND a.power_check = '{0}' AND a.power_check_type = '{1}'
						'''.format(power_check,power_check_type)))
					# t2 = time.time()
					# print('======find cpk use %f sec =====' % (t2 - t1))
					T = []
					nominal = 0
					HighAndLow = []
					total = []
					for data in countCPK:
						if (data[5] >= 0 and data[5] <= ((data[9]+data[10])/2)*50):		#篩選掉明顯有問題的資料
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
					stored_CPK[power_check] = CPK
					isDone = True
					# t3 = time.time()
					# print('======count use %f sec =====' % (t3 - t2))
					print('CPK = ' + str(CPK) + '\n')
					if CPK > 0.67 : 
						stored_sn.append(sn)
						label = '探針或測試點接觸問題' 
					else : label = '程式不穩定'
					countCPK.close()
			else: 
				# countRepairDay = 1		#計算天數 超過7天則直接跳出
				#SFC查找紀錄
				# countRepairDay += 1
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
						SELECT a.*,b.`board` FROM `power_on_result` a
						INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
						WHERE b.board='73-18275-04' AND a.`sn` = '{0}' AND a.`end_time` > '{1}' AND a.`power_check_type` = '{2}'
						GROUP BY `end_time` ORDER BY `end_time` ASC
						'''.format(re_sn,re_time,re_pwr_type)))
					if findRetest_again.rowcount == 0 :   #沒有重測 or SQL query錯誤
						label = '有維修紀錄但無重測紀錄'
						isDone = True
						# print('find RetestAgain Failed')
					else:
						for line_again in findRetest_again :
							if line_again[3] == '00' : 
								Retest_Pass = True
						if Retest_Pass is True :
							label = '零件或製程問題'
						else:
							label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗'
		findRetest.close()

		if CPK == 0 :
			SqlList.append(textwrap.dedent('''
				UPDATE ICT_Project.power_on_result AS a 
				INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
				SET a.sfc_repair = '{0}',a.label = '{1}',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = '{2}'  AND a.power_check_type = '{3}';
				'''.format(sfc_repair,label,sn,power_check_type)))
		else:
			SqlList.append(textwrap.dedent('''
				UPDATE ICT_Project.power_on_result AS a 
				INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
				SET a.sfc_repair = '{0}',a.label = '{1}',a.cpk = '{2}' WHERE b.board='73-18275-04' AND a.sn = '{3}'  AND a.power_check_type = '{4}';
				'''.format(sfc_repair,label,CPK,sn,power_check_type)))
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