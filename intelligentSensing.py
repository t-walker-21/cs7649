import numpy as np

np.random.seed(2)
probs = np.random.random((8,8))
#probs = np.ones((8,8))
debug = np.zeros((8,8))

#print probs.shape
probs[2][4] = 0.3
probs[2][2] = 0.3
probs[1][3] = 0.3
probs[2][3] = 0.3
a = 0
b = 0

for i in range(8):
    for j in range(8):
        print (round(probs[i][j],2)),
    print "\n"

minSenseSquareSum = 1

for i in range(8):
    for j in range(8):
        gridSum = 0
        count = 1.0
        gridSum += probs[i][j]

        if not (i == 0):
            gridSum += probs[i-1][j]
            count += 1

        if not (i == 7):
            gridSum += probs[i+1][j]
            count += 1

        if not (j == 0):
            gridSum += probs[i][j-1]
            count += 1

        if not (j == 7):
            gridSum += probs[i][j+1]
            count += 1

        if ((not i == 0) and (not j == 0)):
            gridSum += probs[i-1][j-1]
            count += 1

        if ((not i == 7) and (not j == 7)):
            gridSum += probs[i+1][j+1]
            count += 1

        if ((not i == 0) and (not j == 7)):
            gridSum += probs[i-1][j+1]
            count += 1
        
        if ((not i == 7) and (not j == 0)):
            gridSum += probs[i+1][j-1]
            count += 1

        debug[i][j] = gridSum / count

        if (debug[i][j] < minSenseSquareSum):
            minSenseSquareSum = debug[i][j]
            a = i
            b = j


print "debug"

for i in range(8):
    for j in range(8):
        print (round(debug[i][j],2)),
    print "\n"


print a,b