
UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22375LU4'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '零件或製程問題',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22361JR6'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22375LJ2'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22375NAH'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22375NGW'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '零件或製程問題',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22375M3C'  AND a.power_check_type = 'pwr_check_pro';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定',a.cpk = '0.0904312467291562' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375MAM'  AND a.power_check_type = 'pwr_check_pro';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22375MR8'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '零件或製程問題',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22375MU1'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22375LBW'  AND a.power_check_type = 'pwr_check_pro';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22375N1N'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22377M5Z'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MQL'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22375LV9'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MJQ'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MJE'  AND a.power_check_type = 'pwr_check_pro';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = 'NULL',a.cpk = '0.0904312467291562' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MF8'  AND a.power_check_type = 'pwr_check_pro';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MJM'  AND a.power_check_type = 'pwr_check_pro';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MM2'  AND a.power_check_type = 'pwr_check_pro';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定',a.cpk = '0.147595460950249' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MDY'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = 'NULL',a.cpk = '0.147595460950249' WHERE b.board='73-18275-04' AND a.sn = 'FOC2238916C'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = 'NULL',a.cpk = '0.147595460950249' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377LNF'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = 'NULL',a.cpk = '0.147595460950249' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377LQ9'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = 'NULL',a.cpk = '0.147595460950249' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MCX'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = 'NULL',a.cpk = '0.0904312467291562' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MDZ'  AND a.power_check_type = 'pwr_check_pro';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22361M1Z'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22334LEZ'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22389194'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC223890DJ'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC223890AV'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC223890B2'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定',a.cpk = '0.200048649062845' WHERE b.board='73-18275-04' AND a.sn = 'FOC223890DW'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22377M6D'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定',a.cpk = '0.338570590374549' WHERE b.board='73-18275-04' AND a.sn = 'FOC223891P7'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '零件或製程問題',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC223890DY'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC223890QD'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22388XLR'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC223890QU'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC223890QB'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22388YNY'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但無重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22388YXJ'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22388ZEC'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '零件或製程問題',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC2238900Q'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22375LG5'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22377M56'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定',a.cpk = '0.342140900920867' WHERE b.board='73-18275-04' AND a.sn = 'FOC22361M1P'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22389J14'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22389JKC'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '零件或製程問題',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22389JEX'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定',a.cpk = '0.504814211213877' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389JFE'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22377LP6'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22388ZQ8'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但無重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC223935FD'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但無重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC223935B3'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22375LBW'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC223935TB'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22401KM4'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22389JTR'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22401KK0'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = 'NULL',a.cpk = '0.342140900920867' WHERE b.board='73-18275-04' AND a.sn = 'FOC22401KLV'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC2239367D'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC2239367J'  AND a.power_check_type = 'pwr_check_pro';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = 'NULL',a.cpk = '0.342140900920867' WHERE b.board='73-18275-04' AND a.sn = 'FOC2239360K'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = 'NULL',a.cpk = '0.0904312467291562' WHERE b.board='73-18275-04' AND a.sn = 'FOC22413SFW'  AND a.power_check_type = 'pwr_check_pro';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = 'NULL',a.cpk = '0.0904312467291562' WHERE b.board='73-18275-04' AND a.sn = 'FOC22413RUM'  AND a.power_check_type = 'pwr_check_pro';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = 'NULL',a.cpk = '0.342140900920867' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403TTY'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22403UJ3'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22413S7X'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但無重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22403UBS'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22403TY0'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22403V0B'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22403UZ6'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但無重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22413S1Q'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = 'NULL',a.cpk = '0.342140900920867' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403VQM'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定',a.cpk = '0.365169276835486' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403U2N'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC224170KD'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC2241705Q'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC224170KJ'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但無重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC224170KJ'  AND a.power_check_type = 'pwr_check_pro';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC2241714D'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC224171CR'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC2241711A'  AND a.power_check_type = 'pwr_check';

UPDATE ICT_Project.power_on_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄',a.cpk = null WHERE b.board='73-18275-04' AND a.sn = 'FOC22401KLB'  AND a.power_check_type = 'pwr_check';
