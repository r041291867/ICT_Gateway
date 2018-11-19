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
	GatewayName = 'BoundaryScan'

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
		SELECT a.*,b.`board` FROM `boundary_scan_result` a 
		INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time AND a.status != 0 WHERE b.board='73-18275-04' 
		GROUP BY a.`sn`,a.`component` ORDER BY `end_time` ASC
		'''))
	SqlList = []
	# print (FulearnCur.rowcount)
	for row in FulearnCur :
		machine = row[0]
		sn = row[1]
		component = row[2]
		status = row[3]
		end_time = row[4]
		seq = row[5]
		sfc_repair = 0
		label = 'NULL'
		isDone = False			#邏輯判斷結束
		#查找是否重測
		Retest_Pass = False
		# print ('find re-test ' + sn)
		findRetest = commonObj.MySqlConn.cursor()
		findRetest.execute(textwrap.dedent('''
			SELECT a.*,b.`board` FROM `boundary_scan_result` a 
			INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
			WHERE b.board='73-18275-04' AND a.sn = '{0}' AND a.component = '{1}' AND a.end_time > '{2}'
			GROUP BY a.end_time ORDER BY `end_time`,`seq` ASC LIMIT 1
			'''.format(sn,component,end_time)))
		isDone = False		#邏輯判斷結束
		re_sn = ''
		re_time = ''
		re_component = ''
		if findRetest.rowcount == 0 :   #沒有重測
			label = '找不到重測紀錄'
		else :			#重測有資料
			for line in findRetest :
				#查找重測是否成功
				re_sn = line[1]
				re_component = line[2]
				re_status = line[3]    #block_status
				re_time = line[4]
				if re_status == '0' : 
					Retest_Pass = True
			if Retest_Pass is True:
				dd3vice = component.split('_')
				findTestjet = commonObj.MySqlConn.cursor()
				findTestjet.execute(textwrap.dedent('''
					SELECT a.*,b.board FROM `testjet_result` a
					INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time
					WHERE b.board='73-18275-04' AND a.sn = '{0}' AND a.device = '{1}'
					GROUP BY a.`sn`
					'''.format(sn,dd3vice[0])))
				if findTestjet.rowcount == 0:
					#計算良率
					countTotal = commonObj.MySqlConn.cursor()
					countTotal.execute(textwrap.dedent('''
						SELECT a.*,b.`board` FROM `boundary_scan_result` a 
						INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
						WHERE b.board='73-18275-04' AND a.component = '{0}'
						Group by end_time ORDER BY `end_time`,`seq` ASC
						'''.format(component)))
					countFail = commonObj.MySqlConn.cursor()
					countFail.execute(textwrap.dedent('''
						SELECT a.*,b.`board` FROM `boundary_scan_result` a 
						INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
						WHERE b.board='73-18275-04' AND a.component = '{0}' AND a.status != 0
						Group by end_time ORDER BY `end_time`,`seq` ASC
						'''.format(component)))
					liang_lu = 1 - (countFail.rowcount/countTotal.rowcount)
					print('良率：' + str(liang_lu))
					if liang_lu > 0.95:			
						label = '探針或測試點接觸問題' + '(' + str(liang_lu) + ')'
					else:
						label = '程式問題' + '(' + str(liang_lu) + ')'
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
					repair_but_failed = False
					findRetest_again = commonObj.MySqlConn.cursor()
					findRetest_again.execute(textwrap.dedent('''
						SELECT a.*,b.`board` FROM `boundary_scan_result` a 
						INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
						WHERE b.board='73-18275-04' AND a.sn = '{0}' AND a.component = '{1}' AND a.end_time > '{2}'
						ORDER BY `end_time`,`seq` ASC
						'''.format(re_sn,re_component,re_time)))
					if findRetest_again.rowcount == 0 :   #沒有重測 or SQL query錯誤
						label = '有維修紀錄但無重測紀錄'
						isDone = True
						# print('find RetestAgain Failed')
					else:
						for line_again in findRetest_again :
							if line_again[3] == '0' : 
								Retest_Pass = True
						if Retest_Pass is True :
							label = '零件或製程問題'
						else:
							label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗'
		findRetest.close()

		SqlList.append(textwrap.dedent('''
			UPDATE ICT_Project.boundary_scan_result AS a 
			INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
			SET a.sfc_repair = '{0}',a.label = '{1}' WHERE b.board='73-18275-04' AND a.sn = '{2}'  AND a.component = '{3}';
			'''.format(sfc_repair,label,sn,component)))
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