#!/bin/bash

## Sources a secondary script which contains a list of parameters and a lists of values.
## This script then loops over each parameter and value, to run a config file,
## prints out the time to run over all events, and logs the run of each iteration.

#source ./RunEverything.sh
VARIABLE=`python RunGeantSettings.py`
echo ${VARIABLE}

cmsRun PPD_RunIISummer20UL17SIM_0_cfg.py ${VARIABLE} >& log1.txt

my_string="Ubuntu;Linux Mint;Debian;Arch;Fedora"
IFS=';' read -ra my_array <<< "$VARIABLE"

#Print the split string
for i in "${my_array[@]}"
do
        echo $i
    done

for PAR in "${!parameters[@]}"; do                # parameter loop
    for VAL in "${!parameters[$PAR]}"; do         # current parameter's values loop
        LOG=log_${PAR}_${VAL}.txt                 # initialize log for the current parameter and value 
        echo $PAR $VAL
        
        cmsRun PPD_RunIISummer20UL17SIM_0_cfg.py paramNames=$PAR paramValues=$VAL >& $LOG     # logs the cmsRun, parsing the current paramter and value
        #python PPD_RunIISummer20UL17SIM_0_cfg.py paramNames=$PAR paramValues=$VAL >& $LOG dump=1  # config dump testing
	echo $VAL $(grep "Total loop" $LOG | tail -n 1 | rev | cut -d' ' -f1 | rev)           # prints the current value and Total loop time of the cmsRun
   done
done

### Old ###
## To run a parameter by the user's input values.
## Make sure to specify your parameter when running ./Script_RunGeantSettings.sh (Parameter)

#echo "Your values: " ;
#read ;
#echo " ";

#for VAL in ${REPLY}; do
#    LOG=Ruslog_${VAL/0./}.txt
#    #ROOT=PPD-RunIISummer20UL17Sim-${VAL/0./}.root
#    #cmsRun varyParam.py $VAL >& $LOG
#    echo $1 $VAL
#    cmsRun PPD_RunIISummer20UL17SIM_0_cfg.py paramNames=$1 paramValues=$VAL >& $LOG
#    echo $VAL $(grep "Total loop" $LOG | tail -n 1 | rev | cut -d' ' -f1 | rev)
#done

