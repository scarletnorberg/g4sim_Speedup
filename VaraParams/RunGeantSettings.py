### imports ###
import os       # to use operating-system-dependent functionalities
import re       # to use regular expressions matching operations

### Values ###

#ProductionCuts = [0.5, 1.0, 2.0, 5.0, 10.0, 12.0, 14.0, 18.0, 20.0]
#Mag_vals = [0.01, 0.015, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35]
RusRo_vals = [0.1, 0.01]
Energy_vals = [200, 250]

### Parameters dictionary ###

parameters = dict()  # initialization the dictionary

## adding key-value pairs 
#parameters['RusRoGammaEnergyLimit']=Energy_vals
#parameters['RusRoElectronEnergyLimit']=Energy_vals

#parameters['RusRoEcalGamma']=RusRo_vals
#parameters['RusRoEcalNeutron']=RusRo_vals


#parameters[('RusRoGammaEnergyLimit','RusRoElectronEnergyLimit')]=Energy_vals

## running at least two parameters and two lists of values for each
parameters['RusRoGammaEnergyLimit, RusRoElectronEnergyLimit']=[Energy_vals,Energy_vals]

### loop ###
for PARAM, VALUES in parameters.items():       # loops key-value pairs
	#for VAL in VALUES:		       # loops the values 
	print(PARAM,VALUES)                    # prints the current parameter and value in the loop
	print(" ")
	VALS1 = VALUES[0]
	VALS2 = VALUES[1]
	
	for VAL1 in VALS1:				    # loops values of the first parameter
		for VAL2 in VALS2:                          # loops values of the second parameter with one value of the first

			PARS = str(PARAM).replace(" ","")                     # makes a string of the parameter list; elimiates spaces
			# make a list of the current value from the first and second parameters
			VALS = str([VAL1, VAL2]).strip("[]").replace(" ","")  # makes a string of the list of values; eliminates brackets and spaces
			print(PARS, VALS)			

			## Parsing
			INPUT = str('paramNames=%s paramValues=%s'%(PARS,VALS))                  # argumets to parse in Running
        		LOG = "log_"+str(PARS).replace(",","_")+"_"+str(VALS).replace(",","_")   # log file for current parameters and values
			
			## Running
			os.system("cmsRun PPD_RunIISummer20UL17SIM_0_cfg.py "+INPUT+" >& "+LOG+".txt")            # cmsRun of config into LOG
			#os.system("python PPD_RunIISummer20UL17SIM_0_cfg.py "+INPUT+" >& "+LOG+".txt dump=1")      # config dump into LOG
		
			## run-time print

			log = open("log_"+str(PARS).replace(",","_")+"_"+str(VALS).replace(",","_")+".txt","r")   # open to read the log file
			run_time = "Total loop"									  # string to search in the log

			for line in log:                         # loop through the all the lines in the log
				if re.search(run_time, line):    
					print(line)              # print the line in the log that contains the specified string
