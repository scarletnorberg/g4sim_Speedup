import glob    # allows to extract the files from a specific directory 
import os
import matplotlib.pyplot as plt
import re

numbers = re.compile(r'(\d+)')
### this function organizes files by their decimal numbers
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

### list where time and changed values are sorted 
changes = []

directory = 'runtest/'  ### directory where the files are located

Files = sorted(glob.glob(directory + '*.txt'), key=numericalSort)
#print(Files)

files_dict = dict()

### for-loop to fill files_dict with each log file in directory
for f in Files:
    files_dict[f] = [] # fill with an empty list for each log file       

#print(files_dict)

### function to get the time loop from the log files
def logline(filename):
    try:
        with open(filename) as logF:
            for line in logF:
                if line.startswith(' - Total loop:'):
                    one = line.find(' ')
                    #two = line.find('s')
                    a = line[one+2:]
                    a = a.replace("Total loop:","")
    except:
        print(filename + " file does not exist.")

    return float(a)


for k,v in files_dict.items():
    v.append(logline(k))      # add total loop value to the respective empty list in files_dict

#print(files_dict)

mark = ['p','s']  # markers for more than one paramter modification

for k,v in files_dict.items():
    #print(changes, "\n")
    filename = k.replace(directory,"")
    param_val = filename.replace("log_","").replace(".txt","")
    param = param_val.strip("_0.123456789")
    val = param_val.strip(param)

    vals_amount = val.count(".") 
    #print(val,vals_amount)

    if vals_amount == 1:   # only one parameter value modified
        #print(val.strip("_"))
        val = val.strip("_")
        changes.append(float(val))
        print("plotting ", param_val)
        plt.plot(changes, v, marker='o', label=param)
        plt.xscale('log')
        plt.xlabel("Changes")
        plt.ylabel("Total Loop")
        plt.title(param+" Time Loop", size=15)
        plt.legend(ncol=1, bbox_to_anchor=(1.1,0), loc='center right', fontsize=7)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(directory+param_val+"_TimeLoop.png")

        plt.close()
        changes.clear()
        #print(changes)
        #print(" ") 
    else:   # two parameter values modified
        #print(val.split("_"))
        vals = val.split("_")
        changes = [float(x) for x in vals]
        for c,m in zip(changes,mark):
            print("plotting", param_val)
            plt.plot(c, v, marker=m, label=param)
        plt.xscale('log')
        plt.xlabel("Changes")
        plt.ylabel("Total Loop")
        plt.title('{}'.format(param), size=15)
        plt.legend(ncol=1, bbox_to_anchor=(1.1,0), loc='center right', fontsize=7)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(directory+param_val+"_TimeLoop.png")

        plt.close()
        changes.clear()
        #print(changes)
        #print(" ")
        

