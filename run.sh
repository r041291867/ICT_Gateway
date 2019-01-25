Env=$1

python ./PowerCheck.py ${Env}

python ./BoundaryScan.py ${Env}

python ./Short.py ${Env}

python ./Open.py ${Env}

python ./Testjet.py ${Env}

python ./AnalogPowered.py ${Env}

python ./Analog.py ${Env}


