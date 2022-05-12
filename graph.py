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
import matplotlib.pyplot as plt

#nested lists
testA = []
testB = []
testC = []
testD = []
testE = []
testF = []

#files
fileA = []
fileB = []
fileC = []
fileD = []
fileE = []
fileF = []
directory = 'run2/'  #directory where files are located

fil = glob.glob(directory + '*.txt')
for file in fil:
    if file.startswith(directory + 'log_RusRoEcalGamma_'):
        fileA.append(file)
    if file.startswith(directory + 'log_RusRoHcalGamma_'):
        fileB.append(file)
    if file.startswith(directory + 'log_RusRoMuonIronGamma_'):
        fileC.append(file)
    if file.startswith( directory + 'log_RusRoEcalNeutron_'):
        fileD.append(file)
    if file.startswith(directory + 'log_RusRoHcalNeutron_'):
        fileE.append(file)
    if file.startswith(directory + 'log_RusRoMuonIronNeutron_'):
        fileF.append(file)

#Files
def files(filename):
    try:
        with open(filename) as f_obj:
            for line in f_obj:
                if line.startswith('('):
                    one = line.find('[')
                    two = line.find(']')
                    a= line[one+1:two]
                    #print(a)
                if line.startswith(' - Total loop:'):
                    one = line.find('  ')
                    b = line[one+2:]
                    #print(b)
    except:
        msg = filename + " file does not exist "
        print(msg)
    return float(a), float(b)

#the for loop executes each of the files in the function
for A,B,C,D,E,F in zip(fileA,fileB,fileC,fileD,fileE,fileF):
    testA.append(files(A))
    testB.append(files(B))
    testC.append(files(C))
    testD.append(files(D))
    testE.append(files(E))
    testF.append(files(F))

#the sorted function organizes the nested lists starting from the first index
testA = sorted(testA,key=lambda x: x[0])
testB = sorted(testB,key=lambda x: x[0])
testC = sorted(testC,key=lambda x: x[0])
testD = sorted(testD,key=lambda x: x[0])
testE = sorted(testE,key=lambda x: x[0])
testF = sorted(testF,key=lambda x: x[0])

#lists where time and change values are stored
x=[]
tA=[]
tB=[]
tC=[]
tD=[]
tE=[]
tF=[]

for A,B,C,D,E,F in zip(testA,testB,testC,testD,testE,testF):    
    x.append(A[0])
    tA.append(A[1])
    tB.append(B[1])
    tC.append(C[1])
    tD.append(D[1])
    tE.append(E[1])
    tF.append(F[1])

#print(x)
#print(tA)
#print(tB)
#print(tC)
#print(tD)
#print(tE)
#print(tF)

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
plt.figure(figsize=(13,6))
plt.plot(x,tA,marker='o',label='RusRoEcalGamma Variation')
plt.plot(x,tB,marker='p',label='RusRoHcalGamma Variation')
plt.plot(x,tC,marker='s',label='RusRoMuonIronGamma Variation')
plt.plot(x,tD,marker='P',label='RusRoEcalNeutron Variation')
plt.plot(x,tE,marker='x',label='RusRoHcalNeutron Variation')
plt.plot(x,tF,marker='v',label='RusRoMuonIronNeutron Variation')
#plt.xscale('log')
plt.xlabel('Changes')
plt.ylabel('Total Loop')
plt.title('{}'.format(p), size = 15)
plt.legend(ncol=1,bbox_to_anchor=(1.1,0),loc='center right',fontsize=7)
plt.grid(True)
plt.tight_layout()
plt.show()
