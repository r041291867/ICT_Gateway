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
	GatewayName = 'Short'

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
	FulearnCur.execute(textwrap.dedent('''
		SELECT a.*,b.`board` FROM `open_short_result` a 
		INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time AND a.status != 0 WHERE b.board='73-18275-04' 
		GROUP BY `sn` ORDER BY `end_time` ASC
		'''))
	SqlList = []
	# print (FulearnCur.rowcount)
	for row in FulearnCur :
		machine = row[0]
		sn = row[1]
		status = row[2]
		end_time = row[3]
		seq = row[4]
		sfc_repair = 0
		label = 'NULL'
		isDone = False			#邏輯判斷結束
		#查找是否重測
		Retest_Pass = False
		# print ('find re-test ' + sn)
		findRetest = commonObj.MySqlConn.cursor()
		findRetest.execute(textwrap.dedent('''
			SELECT a.*,b.board FROM `open_short_result` a
			INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time
			WHERE b.board='73-18275-04' AND a.sn = '{0}' AND a.end_time = '{1}' 
			ORDER BY `seq` ASC 
			'''.format(sn,end_time)))
		isDone = False		#邏輯判斷結束
		re_sn = ''
		re_end_time = ''
		re_seq = ''
		if findRetest.rowcount == 0 :   #沒有重測 or SQL query錯誤
			label = '找不到重測紀錄'
		else :			#重測有資料
			for line in findRetest :
				#查找重測是否成功
				re_sn = line[1]
				re_status = line[2]    #block_status
				re_end_time = line[3]
				re_seq = line[4]
				if re_status == '0' : 
					Retest_Pass = True
			if Retest_Pass is True:
				label = '程式或治具問題'
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
						SELECT a.*,b.board FROM `open_short_result` a
						INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time
						WHERE b.board='73-18275-04' AND a.sn = '{0}' AND a.end_time > '{1}' 
						ORDER BY `seq` ASC 
						'''.format(re_sn,re_end_time)))
					if findRetest_again.rowcount == 0 :   #沒有重測 or SQL query錯誤
						label = '有維修紀錄但無重測紀錄'
						isDone = True
						# print('find RetestAgain Failed')
					else:
						for line_again in findRetest_again :
							if line_again[2] == '0' :
								Retest_Pass = True
						if Retest_Pass is True :
							label = '零件或製程問題'
						else:
							label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗'
		findRetest.close()

		SqlList.append(textwrap.dedent('''
			UPDATE open_short_fail AS a
			INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
			SET sfc_repair = '{0}',label = '{1}' WHERE b.board='73-18275-04' AND a.sn = '{2}' AND fail_type = 'Short';
			'''.format(sfc_repair,label,sn)))
	with open('./Output.sql' ,'wb') as f:
		f.write(bytearray(''.join(SqlList),"utf-8"))
		f.close()
		
	FulearnCur.close()
	
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