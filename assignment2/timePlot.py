#script to read in values from other experiments and plot on graph

import numpy as np
from matplotlib import pyplot as plt

#acquire data
tSS = np.load("standardSearch.npy")
tBT = np.load("backtracking.npy")
tFC = np.load("forwardChecking.npy")

#plot data
plt.plot(tSS,label='SS')
plt.plot(tBT,label='BT')
plt.plot(tFC,label='FC') #the time seems to be equal to BT. plots overlap, but both are being displayed
plt.title('Time Complexity of Different Algos')
plt.xlabel('Num of Queens')
plt.ylabel('Logarithmic Computational Time')
plt.yscale("symlog")
plt.legend(loc='lower right')
plt.show()