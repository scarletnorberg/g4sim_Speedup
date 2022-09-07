#########################################################################################################
##                                                                                                     ##
##                                     Run with python3                                                ##
##  Depending on the run, keep either one or two parameter and their baseline value in baseline_dict   ##
##  Replace the directory string with the directory where your log files are located                   ##
##  On the logline() function, choose the time-loop to be returned; either time[0] or time[1]          ##
##                                                                                                     ##
#########################################################################################################

import glob
import re
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np 


baseline_dict = {"ProductionCut_baseline": 1.0, "RusRoNeutronEnergyLimit_baseline": 10.0}   ## baseline dictionary

directory = 'run10/'  ## directory where files are located

Files = glob.glob(directory + '*.txt')

files_dict = dict()

### for-loop to fill files_dict with each log file in directory ###
for f in Files:
    files_dict[f] = []


### function that returns the parameter values and the desired time-loop of the run ###
def logline(filenames):
    parameter = []
    time = []
    pattern1 = re.compile("PARAMTER")
    pattern2 = re.compile("Total loop:")

    for line in open(filenames):
        for match in re.finditer(pattern1, line):   ## for-loop to find the Parameter
            if line.startswith('('):
                one = line.find('[')
                two = line.find(']')
                a= line[one+1:two]
                parameter.append(float(a))

    for line in open(filenames):
        for match in re.finditer(pattern2, line):
            if line.startswith(' - Total loop:'):  ## for-loop to find the Time Loop
                one = line.find('  ')
                b = line[one+2:]      ## returns two times
                b = float(b)
                time.append(b)

    return parameter, time[1]

### for-loop to store the parameter values and time-loop in the dictionary key's value ###
for k,v in files_dict.items():
    v.append(logline(k))

dict_keys = sorted(files_dict, key=lambda x: x[0])
dict_vals = sorted(files_dict.values(), key=lambda x: x[0])


### function to get the nominal time of a run ###
def base_time(parameter,value,amount):
    #print(parameter, value, amount)
    if amount == 1:     ## single parameter

        for bk,bv in baseline_dict.items():
            bk = bk.replace("_baseline","")

            if re.fullmatch(parameter,bk):
                if value[0][0][0] == bv:
                    nominal = float(value[0][1])
                    return nominal
                break
            break

    else:                 ## double parameter
        basep_list = []
        basev_list = []
        params = parameter.split("_") 
        for bk,bv in baseline_dict.items():
            bk = bk.replace("_baseline","")
            basep_list.append(bk)
            basev_list.append(bv)

        if params.sort()==basep_list.sort():
            if sorted(value[0][0])==sorted(basev_list):
                nominal = float(value[0][1])
                return nominal

### list to plot ###
paramtoplot_list = []

singleparam_values = []
singleparam_time = []

doubleparam_values_x = []
doubleparam_values_y = []
doubleparam_time = []


### for-loop to get the list for plotting ###
for k,v in files_dict.items():
    filename = k.replace(directory,"")
    param_val = filename.replace("log_","").replace(".txt","")
    param = param_val.strip("_0.123456789")
    val = param_val.strip(param)

    vals_amount = val.count(".")
    
    if vals_amount == 1:
        singleparam_values.append(v[0][0][0])
        singleparam_time.append(v[0][1])
    
    else:
        doubleparam_values_x.append(v[0][0][0])
        doubleparam_values_y.append(v[0][0][1])
        doubleparam_time.append(v[0][1])


### to get the nominal times of the runs ###
for k,v in files_dict.items():
    filename = k.replace(directory,"")
    param_val = filename.replace("log_","").replace(".txt","")
    param = param_val.strip("_0.123456789")
    val = param_val.strip(param)

    vals_amount = val.count(".")

    if vals_amount == 1:
        nominal_time = base_time(param,v,vals_amount)
        if type(nominal_time) == float:
            paramtoplot_list.append(param)
            nominalsingletime = [x/nominal_time for x in singleparam_time]

    else: 
        nominal_time = base_time(param,v,vals_amount)
        if type(nominal_time) == float:
            paramtoplot_list.append(param)
            nominaldoubletime = [x/nominal_time for x in doubleparam_time]



for p in paramtoplot_list:
    amount = p.count("_")
    print()

    if amount ==0:
        print("plotting ", p)
        fig = plt.figure(figsize=(8,6))
        plt.xlabel(p, size=15)
        plt.ylabel("Time loop", size=15)
        plt.scatter(singleparam_values,singleparam_time)
        #plt.scatter(singleparam_values, nominalsingletime, color='g')
        plt.savefig(p+"_Timeloop.png")
        plt.close()

    else:
        print("plotting ", p)
        fig = plt.figure(figsize=(8,6))
        axes3d = Axes3D(fig)
        paramlabels = p.split("_")
        z = np.linspace(min(nominaldoubletime),max(nominaldoubletime),num=45)
        plt.xlabel(paramlabels[0], size=15)
        plt.ylabel(paramlabels[1], size=15)
        axes3d.plot(doubleparam_values_x, doubleparam_values_y, nominaldoubletime)
        axes3d.scatter3D(doubleparam_values_x, doubleparam_values_y, nominaldoubletime, color=plt.cm.cool(z/max(z)))
        axes3d.set_zlabel("Time Loop", size=15)
        plt.savefig(p+"_Timeloop.png", bbox_inches="tight")
        plt.close()

