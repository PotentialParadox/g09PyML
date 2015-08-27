__author__ = 'dustintracy'
import numpy as np
import matplotlib.pyplot as plt
import pylab
import scipy.stats as stats

# Open and read the data file
infile = open('tdataH2UNI2.5.dat', 'r')

data = []

for line in infile:
    row = line.strip().split(",")
    data.append(row)

# Truncate and convert to numpy array
data_array = np.array(data)

data = data_array[:-1,[3,15,21]]
data = np.array(data, dtype=float)
data = abs(data)
data_n = data[:,[0,1]]
data_n[:,1] = data[:,2] - data[:,1]

distance = data_n[:,0]
difference = data_n[:,1]

plt.scatter(distance, difference)
plt.xlabel("1")
plt.ylabel("1")
plt.show()


