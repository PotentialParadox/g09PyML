__author__ = 'dustintracy'
import numpy as np
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

data = data_array[:,0:22:3]
A = data[0:2,0:12]
print(A)

