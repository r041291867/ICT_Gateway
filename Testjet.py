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
from decimal import * 

getcontext().prec = 15

class common() :
	MySqlConn = None
	GatewayName = 'Testjet'

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

	FulearnCur = commonObj.MySqlConn.cursor()
	#抓取fail資料
	FulearnCur.execute(textwrap.dedent('''
		SELECT * FROM `testjet_fail`  WHERE board='73-18275-04' 
		GROUP BY `sn`,`device`,`pins` ORDER BY `end_time` ASC
		'''))
	SqlList = []
	# print (FulearnCur.rowcount)
	for row in FulearnCur :
		machine = row[0]
		sn = row[1]
		status = row[2]
		device = row[3]
		end_time = row[4]
		board = row[5]
		fall_no = row[6]
		pins = row[7]
		measured = row[8]
		seq = row[9]
		sfc_repair = 0
		label = 'NULL'
		isDone = False			#邏輯判斷結束
		#查找是否重測
		Retest_Pass = False
		# print ('find re-test ' + sn + ' ' + device)
		findRetest = commonObj.MySqlConn.cursor()
		findRetest.execute(textwrap.dedent('''
			SELECT * FROM `testjet_result`
			WHERE board='73-18275-04' AND `sn` = '{0}' AND `device` = '{1}' AND `end_time` = '{2}'
			ORDER BY `end_time` ASC
			'''.format(sn,device,end_time)))
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
				re_status = line[2]    #block_status
				re_time = line[4]
				if re_status == '00' : 
					Retest_Pass = True
			if Retest_Pass is True:		#查找上下限
				findLimit = commonObj.MySqlConn.cursor()
				findLimit.execute(textwrap.dedent('''
					SELECT * FROM `testjet_limit`
					WHERE board='73-18275-04' AND `board` = '73-18275-04' AND `device` = '{0}' AND `pins` = '{1}'
					'''.format(device,pins)))
				h_limit = 0
				l_limit = 0
				for limit in findLimit:
					l_limit = Decimal(limit[3])
					h_limit = Decimal(limit[4])
				if measured > h_limit:
					label = '程式問題'
				elif measured < l_limit:		#測試步驟良率
					#計算失敗次數
					countFail = commonObj.MySqlConn.cursor()
					countFail.execute(textwrap.dedent('''
						SELECT * FROM `testjet_result` where board = '73-18275-04' and device = 'u84' and status != '00' group by sn,device
						'''.format(device)))
					failTime = countFail.rowcount
					countTotal = commonObj.MySqlConn.cursor()
					countTotal.execute(textwrap.dedent('''
						SELECT * FROM `testjet_result` where board = '73-18275-04' and device = 'u84' group by sn,device
						'''.format(device)))
					totalTime = countTotal.rowcount
					liang_lu = failTime/totalTime
					if liang_lu <= 0.05:
						label = '感應面板或探針問題'
					else:
						label = '程式問題'
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
					# print ('re-test again')
					repair_but_failed = False
					findRetest_again = commonObj.MySqlConn.cursor()
					findRetest_again.execute(textwrap.dedent('''
						SELECT * FROM `testjet_result`
						WHERE board='73-18275-04' AND `sn` = '{0}' AND `device` = '{1}' AND `end_time` > '{2}'
						ORDER BY `end_time` ASC
						'''.format(sn,device,re_time)))
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

		SqlList.append(textwrap.dedent('''
			UPDATE ICT_Project.`testjet_fail` SET sfc_repair = '{0}',label = '{1}' 
			WHERE board='73-18275-04' AND sn = '{2}'  AND device = '{3}';
			'''.format(sfc_repair,label,sn,device)))
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