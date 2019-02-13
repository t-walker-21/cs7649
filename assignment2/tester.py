import numpy as np
from matplotlib import pyplot as plt

tSS = np.load("standardSearch.npy")
tBT = np.load("backtracking.npy")
tFC = np.load("forwardChecking.npy")

plt.plot(tSS)
plt.plot(tBT)
plt.plot(tFC)
plt.yscale("symlog")
plt.show()