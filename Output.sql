
UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375LJ2' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375NGW' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式或治具問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22274QJH' AND a.component = 'b2a' AND a.test_condition = 'b2'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375MR8' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375MU1' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式或治具問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375MK7' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375N1N' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MQL' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377M3J' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式或治具問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377M4J' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.192167969255928)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377M5J' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.192167969255928)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375N49' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.192167969255928)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MHJ' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.192167969255928)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MS3' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.192167969255928)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377M3C' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377LMY' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.192167969255928)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377LXU' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375LV9' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.192167969255928)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22313WPE' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.192167969255928)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22361LG5' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22361JW5' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.192167969255928)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377LSZ' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.192167969255928)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MDX' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.192167969255928)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MCU' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377LSQ' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MMA' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.192167969255928)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MFY' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377LQR' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377LTR' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MFP' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MJQ' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC223890RV' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375MLH' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.488430208194506)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375MHB' AND a.component = 'b2a' AND a.test_condition = 'b2'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗' WHERE b.board='73-18275-04' AND a.sn = 'FOC22361M1Z' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389194' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC223891W7' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.00872283096442284)' WHERE b.board='73-18275-04' AND a.sn = 'FOC223891WB' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC223891TQ' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.00872283096442284)' WHERE b.board='73-18275-04' AND a.sn = 'FOC223890AV' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC223891UA' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.00872283096442284)' WHERE b.board='73-18275-04' AND a.sn = 'FOC223891NL' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.00872283096442284)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375MVJ' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.00872283096442284)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MW1' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.00872283096442284)' WHERE b.board='73-18275-04' AND a.sn = 'FOC223891LL' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.00872283096442284)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377MNW' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.00872283096442284)' WHERE b.board='73-18275-04' AND a.sn = 'FOC223891GA' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.00872283096442284)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389197' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.00872283096442284)' WHERE b.board='73-18275-04' AND a.sn = 'FOC223891HT' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '探針或測試點接觸問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389198' AND a.component = 'u37' AND a.test_condition = 'OUT'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.00872283096442284)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377LQ4' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗' WHERE b.board='73-18275-04' AND a.sn = 'FOC223891LE' AND a.component = 'u37' AND a.test_condition = 'OUT'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '探針或測試點接觸問題(0.997492963449306)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377N0K' AND a.component = 'u37' AND a.test_condition = 'OUT'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388WRB' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388X96' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388XLR' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.00872283096442284)' WHERE b.board='73-18275-04' AND a.sn = 'FOC223890S8' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388WJ8' AND a.component = 'b2a' AND a.test_condition = 'b2'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.488430208194506)' WHERE b.board='73-18275-04' AND a.sn = 'FOC223891LZ' AND a.component = 'b2a' AND a.test_condition = 'b2'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.192167969255928)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388X35' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388YNY' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388ZEC' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '零件或製程問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC2238900Q' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375LMU' AND a.component = 'b2a' AND a.test_condition = 'b2'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377M56' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.488430208194506)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22313WYZ' AND a.component = 'b2a' AND a.test_condition = 'b2'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.192167969255928)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22361M1P' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.00872283096442284)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389J13' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389JKV' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389J5S' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22377LP6' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.488430208194506)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389JAM' AND a.component = 'b2a' AND a.test_condition = 'b2'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.488430208194506)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389JDN' AND a.component = 'b2a' AND a.test_condition = 'b2'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22388ZQ8' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但無重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC223935FD' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗' WHERE b.board='73-18275-04' AND a.sn = 'FOC22375LBW' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC223935B3' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗' WHERE b.board='73-18275-04' AND a.sn = 'FOC223935TB' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '探針或測試點接觸問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389JXQ' AND a.component = 'u28' AND a.test_condition = 'OUT'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22401KM4' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '探針或測試點接觸問題(2.06192486366798)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389JYW' AND a.component = 'u28' AND a.test_condition = 'OUT'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.192167969255928)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22401KLV' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '零件或製程問題' WHERE b.board='73-18275-04' AND a.sn = 'FOC22389JC4' AND a.component = 'b2a' AND a.test_condition = 'b2'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC2239367D' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.192167969255928)' WHERE b.board='73-18275-04' AND a.sn = 'FOC2239360K' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22413BV4' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22413BVB' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.00872283096442284)' WHERE b.board='73-18275-04' AND a.sn = 'FOC2239365A' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.00872283096442284)' WHERE b.board='73-18275-04' AND a.sn = 'FOC2239365L' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.00872283096442284)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22413BVQ' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.192167969255928)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403TTY' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403UJ3' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但沒有維修後重測紀錄or維修後仍重測失敗' WHERE b.board='73-18275-04' AND a.sn = 'FOC22413S7X' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但無重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22413RVL' AND a.component = 'b2a' AND a.test_condition = 'b2'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但無重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403UBS' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403TY0' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403V0B' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403UZ6' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '1',a.label = '有維修紀錄但無重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22413S1Q' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.192167969255928)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403VQM' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.192167969255928)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403U2N' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC2241705Q' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC224170KJ' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC224170YF' AND a.component = 'fmgy1' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC2241714D' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC224171CR' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '程式不穩定(0.00872283096442284)' WHERE b.board='73-18275-04' AND a.sn = 'FOC22403VTH' AND a.component = 'u17' AND a.test_condition = 'Pin3'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '無維修紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC2241711A' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'

UPDATE ICT_Project.analog_powered_result AS a 
INNER JOIN ict_result b ON a.machine=b.machine AND a.sn=b.sn AND a.end_time=b.end_time 
SET a.sfc_repair = '0',a.label = '找不到重測紀錄' WHERE b.board='73-18275-04' AND a.sn = 'FOC22401KLB' AND a.component = 'u77_freq' AND a.test_condition = 'Freq_out'
