### imports ###
import os       # to use operating-system-dependent functionalities
import re       # to use regular expressions matching operations
from collections import OrderedDict
from copy import deepcopy

### Values ###

#ProductionCuts = [0.5, 1.0, 2.0, 5.0, 10.0, 12.0, 14.0, 18.0, 20.0]
#Mag_vals = [0.01, 0.015, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35]
EnergyThSimple_vals = [0.01, 0.015, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
Energy_vals = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 65, 70, 75, 80, 85, 90, 95, 100, 200, 300]


### function for recursive for-loops ###

## The function takes 5 arguments, the position, a list of parameters,
## two empty lists to be filled: one for parameters, the other for values,
## and an empty set to be filled with the possible combination of values


def varyAll(pos,paramlist,pars,sig,sigs):
    param = paramlist[pos][0]
    vals = paramlist[pos][1]
    
    for v in vals:            # for-loops the values list
        stmp = sig[:]+[v]     # the current value in for-loop    
        
	if param not in pars:    # checks to see if parameter is in list
	    pars.append(param)   # adds parameter to list
     
	# check if last param
        if pos+1==len(paramlist):
            sigs.add(tuple(stmp))
        else:
            varyAll(pos+1,paramlist,pars,stmp,sigs)
    
    parameters = pars	
    values = sigs
    print (parameters, values)
    return(parameters,values)



## running at least two parameters and two lists of values for each

params = OrderedDict([
	("EnergyThSimple", EnergyThSimple_vals),
	("RusRoNeutronEnergyLimit", Energy_vals)
])

parameters = []
sigs = set()

varyAll(0,list(params.iteritems()),parameters,[],sigs)
print("")

# for-loops the set of values
for VALS in sigs:
	print(parameters, VALS)
	print(" ")
	PARS = str(parameters).strip("[]").replace(" ","").replace("'","")       # makes a string of the parameter list; elimiates unwanted characters
	VALS = str(VALS).strip("()").replace(" ","")                             # makes a string of the list of values; eliminates unwanted characters

	## Parsing
	INPUT = str('paramNames=%s paramValues=%s'%(PARS,VALS))                  # argumets to parse in Running
	LOG = "log_"+str(PARS).replace(",","_")+"_"+str(VALS).replace(",","_")   # log file for current parameters and values

	## Running
	os.system("cmsRun PPD_RunIISummer20UL17SIM_0_cfg.py "+INPUT+" >& "+LOG+".txt")            # cmsRun of config into LOG
	#os.system("python PPD_RunIISummer20UL17SIM_0_cfg.py "+INPUT+" >& "+LOG+".txt dump=1")      # config dump into LOG

		
	## run-time print

	log = open("log_"+str(PARS).replace(",","_")+"_"+str(VALS).replace(",","_")+".txt","r")   # open to read the log file
	run_time = "Total loop"								          # string to search in the log

	for line in log:                         # loop through the all the lines in the log
		if re.search(run_time, line):    
			print(line)              # print the line in the log that contains the specified string

