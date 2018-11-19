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

	FulearnCur = commonObj.MySqlConn.cursor()
	#抓取fail資料
	FulearnCur.execute(textwrap.dedent('''
		SELECT a.*,b.`board` FROM `power_on_result` a 
		INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time AND a.status != 0 WHERE b.board='73-18275-04' 
		GROUP BY `sn`,`power_check_type` ORDER BY `end_time` ASC
		'''))
	SqlList = []
	print (FulearnCur.rowcount)
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
		label = 'NULL'
		isDone = False			#邏輯判斷結束
		isNDF_Day = 1
		noRecord_Day = 1
		while True: #如果是NDF/沒有sfc紀錄則跳到這裡重測
			#查找是否重測
			if noRecord_Day == 7:
				isDone = True
				label = '無維修紀錄'
				break
			if isNDF_Day == 7:
				isDone = True
				label = 'NPF'
				break
			print ('find re-test ' + sn)
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
				label = '資料不足'
				print('find Retest Failed')
				break
			for line in findRetest :
				#查找重測是否成功
				print('if re-test success?')
				re_sn = line[1]
				re_pwr_type = line[2]
				re_status = line[3]    #block_status
				re_time = line[11]
				if re_status == '00' : 
					print('Yes')
					label = '程式或治具問題'
					isDone = True
					break
				print('No')
			if isDone is True: break

			countRepairDay = 1		#計算天數 超過7天則直接跳出
			#SFC查找紀錄
			while True:		#沒有維修紀錄則24小時後再來查詢
				print ('find SFC record ' + str(countRepairDay))
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
					#Etime = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')  
					#往前抓１天 往後抓７天
					delta1 = datetime.timedelta(days=1)
					delta7 = datetime.timedelta(days=7)
					startTime = str(end_time - delta1)[:10]
					endTime = str(end_time + delta7)[:10]
					# startTime = '2018-09-21'
					# endTime = '2018-10-15'
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
					noRecord_Day += 1
				elif isNDF is True: 
					isNDF_Day += 1 
					break
				else:
					#查找是否重測(第二次)
					print ('re-test again')
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
						print('find RetestAgain Failed')
						break
					for line_again in findRetest_again :
						if line_again[3] == '00' : 
							Retest_Pass = True
							repair_but_failed = False
							label = '零件或製程問題'
							isDone = True
							break
						else:
							repair_but_failed = True
					if repair_but_failed is True :
						label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗'
						isDone = True
						break

				if has_record == True : break	
				if isDone is True : break	
			if isDone is True : break	
			findRetest.close()

		SqlList.append(textwrap.dedent('''
			UPDATE ICT_Project.power_on_result SET sfc_repair = '{0}',label = '{1}' WHERE seq = '{2}';
			'''.format(sfc_repair,label,seq)))
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
	
	
main()
Fetch()