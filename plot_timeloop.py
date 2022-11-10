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
from mpl_toolkits import mplot3d
import numpy as np 


baseline_dict = {"ProductionCut_baseline": 1.0, "RusRoNeutronEnergyLimit_baseline": 10.0}   ## baseline dictionary

directory = 'run5b/'  ## directory where files are located

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
                ## time[0] is the run total time loop; time[1] is the CPU total loop

    return parameter, time[1]

### for-loop to store the parameter values and time-loop in the dictionary key's value ###
for k,v in files_dict.items():
    v.append(logline(k))

dict_keys = sorted(files_dict, key=lambda x: x[0])
dict_vals = sorted(files_dict.values(), key=lambda x: x[0])


### function to get the nominal time of a run ###
def base_time(parameter,value,amount):
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

nominalsingletime = []
nominaldoubletime = []

nominaltime = 0.0   # place-holder to replace with the nominal time of the chosen run
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
            nominaltimeratio = [x/nominal_time for x in singleparam_time]
            nominaltime = nominal_time
            nominalPV = param_val

    else: 
        nominal_time = base_time(param,v,vals_amount)
        if type(nominal_time) == float:
            paramtoplot_list.append(param)
            nominaltimeratio = [x/nominal_time for x in doubleparam_time]
            nominaltime = nominal_time
            nominalPV = param_val


print("The nominal run - ",nominalPV," - time is ", nominaltime)
print()

for d,t in zip(files_dict.items(),nominaltimeratio):  ## add the nominal time ratio to the corresponding files_dict value
    d[1].append(t)

## for-loop for table of parameter, values, CPU time and ratio time
print("||   Parameters_Values   ||   CPU Time   ||   Ratio-Time   ||")
print("----------------------------------------------------------------------------")
for k,v in files_dict.items():
    filename = k.replace(directory,"")
    param_val = filename.replace("log_","").replace(".txt","")
    param = param_val.strip("_0.123456789")
    val = param_val.strip(param)

    print(param_val," || ", v[0][1], " || ",v[1])

### plotting ###        
for p in paramtoplot_list:
    amount = p.count("_")
    print()

    if amount ==0:
        print("plotting ", p)

        fig = plt.figure(figsize=(8,6))
        plt.xlabel(p, size=15)
        plt.ylabel("Time loop", size=15)
        scatter = plt.scatter(singleparam_values, singleparam_time, c=nominaltimeratio, cmap='hot')

        plt.colorbar(scatter, label="Time Loop ratio")
        plt.savefig(p+"_Timeloop.png")
        plt.close()

    else:
        print("plotting ", p)

        fig = plt.figure(figsize=(8,6))
        ax = plt.axes(projection = "3d")
        paramlabels = p.split("_")

        color_map = plt.get_cmap('hot')

        z = np.linspace(min(nominaltimeratio),max(nominaltimeratio),num=45)
        plt.xlabel(paramlabels[0], size=12)
        plt.ylabel(paramlabels[1], size=12)
        line = ax.plot3D(doubleparam_values_x, doubleparam_values_y, nominaltimeratio)
        scatter = ax.scatter3D(doubleparam_values_x, doubleparam_values_y, nominaltimeratio, c=nominaltimeratio,cmap=color_map)

        ax.set_zlabel("Time Loop", size=12)
        plt.colorbar(scatter)
        plt.savefig(p+"_Timeloop.png")
        plt.close()

