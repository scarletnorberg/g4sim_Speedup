import glob
import re
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np 

fileA = []
test = []


directory = 'run8/'  #directory where files are located
#di = 'run8a/'

fil = glob.glob(directory + '*.txt')
for file in fil:
    if file.startswith(directory + 'log_EnergyThSimple_RusRoGammaEnergyLimit_'):
        fileA.append(file)

#fil_a = glob.glob(di + '*.txt')
#for file in fil_a:
#    if file.startswith(di + 'log_EnergyThSimple_RusRoGammaEnergyLimit_'):
#        fileA.append(file)

def files(filenames):
    l = []
    pattern1 = re.compile("PARAMTER")
    pattern2 = re.compile("Total loop:")

    for line in open(filenames):
        for match in re.finditer(pattern1, line):
            if line.startswith('('):
                one = line.find('[')
                two = line.find(']')
                a= line[one+1:two]
                l.append(float(a))

    for line in open(filenames):
        for match in re.finditer(pattern2, line):
            if line.startswith(' - Total loop:'):
                one = line.find('  ')
                b = line[one+2:]
                #print(b)
    return l, float(b)

for A in fileA:
    test.append(files(A))

test = sorted(test,key=lambda x: x[0])
#print(test)

changes = []
x = []
y = []
z = []

for a in test:
    changes.append(a[0])
    z.append(a[1])

for b in changes:
    x.append(b[0])
    y.append(b[1])

#dividing by the value nominal
z1 = []

for A in z:
    z1.append(A/z[1])

print(x)
print(y)
print(z)
print(z1)

fig = plt.figure(figsize=(8,6))
axes3d = Axes3D(fig)
axes3d.plot(x,y,z1)
axes3d.scatter3D(x,y,z1)
plt.xlabel('EnergyThSimple',size = 15)
plt.ylabel('RusRoNeutronEnergyLimit',size = 15)
axes3d.set_zlabel('Time Loop',size=15)
plt.savefig('combine2.png', bbox_inches="tight")
