#This crypt allows you to extract the data from a file and graph it.
#Below you will find a guide to the output events from which you can take the values to plot.

#TimeReport> Time report complete in 616.751 seconds
# Time Summary:
# - Min event:   14.4966
# - Max event:   175.726
# - Avg event:   95.1116
# - Total loop:  541.517
# - Total init:  57.3865
# - Total job:   616.751
# - EventSetup Lock:   0.150529
# - EventSetup Get:   202.964
# Event Throughput: 0.00369333 ev/s
# CPU Summary:
# - Total loop:  60.1669
# - Total init:  7.58007
# - Total extra: 0
# - Total job:   68.0555
# Processing Summary:
# - Number of Events:  2
# - Number of Global Begin Lumi Calls:  1
# - Number of Global Begin Run Calls: 1

from pathlib import Path
import os
import matplotlib.pyplot as plt

#lists where time and change values are stored
time = []
changes = []

#files
filenames = []
directory = 'run4' #directory where files are located

fil = Path(directory).glob('*')
for file in fil:
        if str(file).startswith('run4/log_DeltaChordSimple_'):
                filenames.append(file)

#reading multiple files through one function
def files(filename):
        try:
                with open(filename) as f_obj:
                        for line in f_obj:
                                if line.startswith(' - Total loop:'):
                                        one = line.find('  ')
                                        #two = line.find('s')
                                        a = line[one+2:]
        except:
                msg = filename + " file does not exist "
                print(msg)
        return time.append(float(a))

#the for loop executes each of the files in the function
for filename in filenames:
        files(filename)

#list of  the file names
names = []
for files in os.listdir(directory):
        if files.startswith('log_DeltaChordSimple'):
                names.append(files)

#in this loop the value of the changes are extracted
for value in names:
        th = value.find('e_')
        fr = value.find('x')
        b = value[th+2:fr-2]
        changes.append(float(b))

#Parameters, if you need to use any of them to produce the graph you just have to uncomment
#p = 'EnergyThSimple'
#p = 'DeltaOneStepSimple'
p = 'DeltaChordSimple'
#p = 'RusRoGammaEnergyLimit'
#p = 'RusRoNeutronEnergyLimit'
#p = 'RusRoEcalGamma'
#p = 'RusRoHcalGamma'

#graphing the behavior of the parameter
plt.plot(changes,time,marker='o',label='Time Variation')
plt.xlabel('Changes')
plt.ylabel('Total Loop')
plt.title('{}'.format(p), size = 15)
plt.legend()
plt.grid()
plt.show()
