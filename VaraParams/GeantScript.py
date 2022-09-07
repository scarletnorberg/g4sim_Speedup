########################################################################################################
##                                                                                                    ##
##                                          run with python                                           ##
##  Replace the options.inputroot string with the desired run                                         ##
##  Add a list of values for the parameters, with the name of the variable like NAME_vals             ##
##  Add the parameters (as key) and the list of vlues (as the key's value) to the params OrderedDict  ##
##  and keep either a single or two items in the OrderedDict                                          ##
##                                                                                                    ##
########################################################################################################

### imports ###
import os    # to use operating-system-dependent functionalities
import re    # to use regular expressiones for matching operations
from collections import OrderedDict
from copy import deepcopy
from g4SimHit_SpeedUp.VarParameters.optGenSim import options

### Input to Config ###
options.inputroot = "PPD-RunIISummer20UL17GEN-00001"


### Values ### 
ProdCuts_vals = [0.5, 1.0, 2.0, 5.0, 10.0, 12.0, 14.0, 18.0, 20.0]
EnergyThSimple_vals = [0.015, 0.1, 0.3, 0.6, 1.0]
#RRNeutronEnergy_vals = [0.0, 10.0, 30.0, 30.0, 60.0, 60.0, 200.0]


### Parameters and values ###
params = OrderedDict([
         #("RusRoNeutronEnergyLimit", RRNeutronEnergy_vals),
         ("EnergyThSimple", EnergyThSimple_vals),
         ("ProductionCut", ProdCuts_vals)
])

### function to return a set of combinations of the parameter values ### 
#
## The function takes 5 arguments: 
## the "position" of a given parameter_value dictionary, 
## the iteritems of a dictionary of parameters,
## two empty lists to be filled within the function: one for the parameters, the other for the values,
## and an empty set-object to be filled with the possible combination of the given values
#

def ParamValsRun(pos,paramvalist,pars,sig,valset):
    param = paramvalist[pos][0]  # key from paramvalist.iteritems()
    vals = paramvalist[pos][1]   # value from paramvalist.iteritems()

    for v in vals:
        stmp = sig[:]+[v] # stamp of the current value in this for-loop

        if param not in pars:  # checks to see if parameter is in list 
            pars.append(param) # if not, add it to the pars list

        # check if it's the last parameter in the iteration
        if pos+1==len(paramvalist):
            valset.add(tuple(stmp))  # if so, fill the set-object
        else:
            ParamValsRun(pos+1,paramvalist,pars,stmp,valset) # if not, call the function to continue

    parameters = pars
    values = valset
    print(parameters, values)
    return(parameters, values)

parameters = []
values = set()

ParamValsRun(0, list(params.iteritems()), parameters, [], values)

## For a single parameter with one or more value(s)
if len(parameters)==1:
    for VALS in params.values():
        for v in VALS:
            PAR = str(params.keys()).strip("[]").replace(" ","").replace("'","")
            VAL = str(v).strip("()").replace(" ","")
            print(PAR,VAL)
            print()
            ## Parsing
            INPUT = str('inputroot=%s paramNames=%s paramValues=%s'%(options.inputroot,PAR,VAL)) # arguments to parse in Running
            LOG = "log_"+str(PAR).replace(",","_")+"_"+str(VAL).replace(",","_")                 # log file for current parameters and values

            ## Running
            os.system("cmsRun PPD_RunIISummer20UL17SIM_0_cfg.py "+INPUT+" >& "+LOG+".txt")   # cmsRun of desired config file; dumped into LOG

            ## run-time print
            log = open("log_"+str(PAR).replace(",","_")+"_"+str(VAL).replace(",","_")+".txt","r")   # open to read the log file

            run_time = "Total loop"   # string to search in log

            for line in log:
                if re.search(run_time, line):
                    print(line)

## For a combination of parameters
elif len(parameters)>=2:
    for VALS in values:         ## for-loop the set of values
        print(parameters, VALS)
        print()
        PARS = str(parameters).strip("[]").replace(" ","").replace("'","")
        VALS = str(VALS).strip("()").replace(" ","")

        ## Parsing
        INPUT = str('inputroot=%s paramNames=%s paramValues=%s'%(options.inputroot,PARS,VALS)) # arguments to parse in Running
        LOG = "log_"+str(PARS).replace(",","_")+"_"+str(VALS).replace(",","_")                 # log file for current parameters and values

        ## Running
        os.system("cmsRun PPD_RunIISummer20UL17SIM_0_cfg.py "+INPUT+" >& "+LOG+".txt")   # cmsRun of desired config file; dumped into LOG

        ## run-time print
        log = open("log_"+str(PARS).replace(",","_")+"_"+str(VALS).replace(",","_")+".txt","r")   # open to read the log file

        run_time = "Total loop"   # string to search in log

        for line in log:
            if re.search(run_time, line):
                print(line)
