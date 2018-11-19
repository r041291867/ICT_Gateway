
UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375LWQ'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375LWZ'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375MV3'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375NKQ'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375NE9'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375MPK'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375NL8'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '零件或製程問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375L9L'  AND a.component = 'u29_fmgu3';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '零件或製程問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375L9L'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375NLH'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375MED'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377M61'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375MEX'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375N4N'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375LY6'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MSA'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC223890RJ'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MFW'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377M05'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '零件或製程問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC223890XX'  AND a.component = 'u29_fmgu3';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '零件或製程問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC223890XX'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '零件或製程問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375L99'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375LM3'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377LYR'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MC9'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MC9'  AND a.component = 'u29_fmgu3';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22334KS8'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377NA0'  AND a.component = 'u29_fmgu3';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377NA0'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MW6'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377M2U'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22361LXM'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC223890XU'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377N50'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC223891VV'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC223891HN'  AND a.component = 'u29_fmgu3';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC223891HN'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗' WHERE b.board='73-18275-04' AND a.sn = 'FOC223890CA'  AND a.component = 'u29_fmgu3';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗' WHERE b.board='73-18275-04' AND a.sn = 'FOC223890CA'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC223890XW'  AND a.component = 'u21_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388WQD'  AND a.component = 'u29_fmgu3';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388WQD'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377N1N'  AND a.component = 'u23_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC223891JJ'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC223890Q0'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388WKK'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC223890DE'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388XML'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377N2C'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377LS5'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377LS5'  AND a.component = 'u29_fmgu3';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388X8D'  AND a.component = 'u18_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388XMN'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388YL3'  AND a.component = 'u23_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388YC9'  AND a.component = 'u23_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388YA6'  AND a.component = 'u29_fmgu3';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388YA6'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388ZDM'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388ZS0'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388ZE3'  AND a.component = 'u23_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但無重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388YPA'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389J3W'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389J3N'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389J6U'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389J02'  AND a.component = 'u23_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389HU8'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389HWZ'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389JKV'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389JK2'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389J71'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389J1A'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389JB3'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389J3P'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389J4W'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389J4J'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389J2Y'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389HX4'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但無重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389HPX'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388ZF1'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC223935PH'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389JYF'  AND a.component = 'u20_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC223935PQ'  AND a.component = 'u19_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC223935C2'  AND a.component = 'u19_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC223935BM'  AND a.component = 'u19_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC223935CN'  AND a.component = 'u19_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC223936H5'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC2239364C'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22413BTW'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC223936MB'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22413BT5'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但無重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC223936DQ'  AND a.component = 'u29_fmgu3';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但無重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC223936DQ'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22413BQW'  AND a.component = 'u18_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC223936EP'  AND a.component = 'u18_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC2239367E'  AND a.component = 'u18_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22413BSN'  AND a.component = 'u18_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22413BSN'  AND a.component = 'u19_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22393674'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC223936DP'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22361LXM'  AND a.component = 'u29_fmgu3';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22361LXM'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389194'  AND a.component = 'u29_fmgu3';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389194'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22413C0J'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC223935TG'  AND a.component = 'u29_fmgu3';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC223935TG'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC2239365J'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22413RX6'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22413SD9'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22413S5B'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403TZL'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22413RQK'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但無重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403TXJ'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403TJS'  AND a.component = 'u23_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403TZF'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403TQN'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403U7J'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403UBS'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403UBY'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403UH0'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403U75'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403U3J'  AND a.component = 'u23_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403U3J'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403TV5'  AND a.component = 'u29_fmgu3';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403TV5'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403TVW'  AND a.component = 'u29_fmgu3';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403TVW'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22417042'  AND a.component = 'u18_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '零件或製程問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22417043'  AND a.component = 'u18_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403UFJ'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403UWM'  AND a.component = 'u23_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403U3B'  AND a.component = 'u23_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403TXQ'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC224170GD'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC224170HC'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC224170G7'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC224170HB'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC224170AU'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC224170JL'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但無重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC224170AP'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC224170EK'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC224170ER'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗' WHERE b.board='73-18275-04' AND a.sn = 'FOC224170E8'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403V57'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403USJ'  AND a.component = 'fmgu3_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC224170B4'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC224170AV'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC224170UU'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403UT1'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC224170S0'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403VR9'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403VCY'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403VP5'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403V7B'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題(0.9873318532062165)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22417170'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403VP1'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC2241717T'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403VPD'  AND a.component = 'u21_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403VPD'  AND a.component = 'u22_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403VPD'  AND a.component = 'u23_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403VPD'  AND a.component = 'fmgu3_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403VPD'  AND a.component = 'u18_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403VPD'  AND a.component = 'u19_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403VPD'  AND a.component = 'u20_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '零件或製程問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403U2Y'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403VFX'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但無重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403VM4'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但無重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403VM4'  AND a.component = 'u29_fmgu3';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403VXH'  AND a.component = 'u73_connect';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22417156'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗' WHERE b.board='73-18275-04' AND a.sn = 'FOC22417125'  AND a.component = 'u29_fmgu3_aio';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC224170PH'  AND a.component = 'u29_fmgu3';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375MV3'  AND a.component = 'u29_fmgu3';

UPDATE ICT_Project.boundary_scan_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22334KVS'  AND a.component = 'u73_connect';
