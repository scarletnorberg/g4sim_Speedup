import matplotlib.pyplot as plt
from numpy import loadtxt

#lists where time and change values are stored
time = []
changes = []

#reading the .txt file
graph = loadtxt("changes_RusRoEcalGamma.txt",float)
for row in graph:
    time.append(float(row[0]))
    changes.append(float(row[1]))

#graphing the behavior of the parameter
plt.plot(time,changes)
plt.xlabel('Changes')
plt.ylabel('Total loop')
plt.title('RusRoEcalGamma', size = 15)
plt.show()
