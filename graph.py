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

import glob 
import os
import matplotlib.pyplot as plt
import re

#this function allows you to organize files by their decimal numbers
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

#lists where time and change values are stored
timeA = []
timeB = []
timeC = []
timeD = []
timeE = []
timeF = []
changes = []

#files
fileA = []
fileB = []
fileC = []
fileD = []
fileE = []
fileF = []
directory = 'run2/'  #directory where files are located

fil = sorted(glob.glob(directory + '*.txt'), key=numericalSort) #the glob library allows extracting the files from a specific directory and the sorted function organizes the files
for file in fil:
    if file.startswith('run2/log_RusRoEcalGamma_'):
        fileA.append(file)
    if file.startswith('run2/log_RusRoHcalGamma_'):
        fileB.append(file)
    if file.startswith('run2/log_RusRoMuonIronGamma_'):
        fileC.append(file)
    if file.startswith('run2/log_RusRoEcalNeutron_'):
        fileD.append(file)
    if file.startswith('run2/log_RusRoHcalNeutron_'):
        fileE.append(file)
    if file.startswith('run2/log_RusRoMuonIronNeutron_'):
        fileF.append(file)

#Files_A
def files_A(filename):
	try:
		with open(filename) as f_obj:
			for line in f_obj:
				if line.startswith(' - Total loop:'):
					one = line.find('  ')
					#two = line.find('s')	
					a = line[one+2:]
					#print(a)
	except:
		msg = filename + " file does not exist "
		print(msg)
	return float(a)

#the for loop executes each of the files in the function
for A,B,C,D,E,F in zip(fileA,fileB,fileC,fileD,fileE,fileF):
    timeA.append(files_A(A))
    timeB.append(files_A(B))
    timeC.append(files_A(C))
    timeD.append(files_A(D))
    timeE.append(files_A(E))
    timeF.append(files_A(F))

#in this loop the value of the changes are extracted
for value in fileA:
	th = value.find('a_')
	fr = value.find('x')
	b = value[th+2:fr-2]
	changes.append(float(b))
	#print(value[th])

#print(changes)
#print(timeA)
#print(timeB)
#print(timeC)
#print(timeD)
#print(timeE)
#print(timeF)

#Parameters, if you need to use any of them to produce the graph you just have to uncomment
#p = 'EnergyThSimple'
#p = 'DeltaOneStepSimple'
#p = 'DeltaChordSimple'
#p = 'RusRoGammaEnergyLimit'
#p = 'RusRoNeutronEnergyLimit'
#p = 'RusRoEcalGamma'
#p = 'RusRoHcalGamma'
#p = 'RusRoMuonIronNeutron'
#p = 'ProductionCut'
#p = 'Energy Parameters'
#p = 'Magnetic Parameters'
p = 'Probability Parameters'

#graphing the behavior of the parameter
plt.plot(changes,timeA,marker='o',label='RusRoEcalGamma Variation')
plt.plot(changes,timeB,marker='p',label='RusRoHcalGamma Variation')
plt.plot(changes,timeC,marker='s',label='RusRoMuonIronGamma Variation')
plt.plot(changes,timeD,marker='P',label='RusRoEcalNeutron Variation')
plt.plot(changes,timeE,marker='x',label='RusRoHcalNeutron Variation')
plt.plot(changes,timeF,marker='v',label='RusRoMuonIronNeutron Variation')
plt.xscale('log')
plt.xlabel('Changes')
plt.ylabel('Total Loop')
plt.title('{}'.format(p), size = 15)
plt.legend(ncol=1,bbox_to_anchor=(1.1,0),loc='center right',fontsize=7)
plt.grid(True)
plt.tight_layout()
plt.show()
