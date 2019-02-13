import numpy as np
import time
import copy
import sys
TIME_LIM = 10 * 60 
from matplotlib import pyplot as plt

def checkLen(queens):
    return len(queens.split(','))


def visualizeQueens(queens):
    tempGrid = np.zeros([len(queens),len(queens)])
    
    count = 0
    for q in queens:
        tempGrid[int(q)][count] = 1
        count += 1
    
    print tempGrid


def checkConsistency(queens):
    #enumerate queen coordinates
    queenCoords = []
    count = 0
    for q in queens:
        queenCoords.append((count,int(q)))
        count += 1
    #print queenCoords

    #check constraints for each queen coordinate
    
    index = 0
    
    for q in queenCoords:
        #print "checking -->" , q
        tempList = copy.copy(queenCoords)
        tempList.remove(tempList[index]) #first make a list of coordinates without the queen we're checking
        #print tempList

        
        #check same row and column and diagonal
        for n in tempList:
            if (n[1] == q[1] or (abs(n[0] - q[0]) == abs(n[1] - q[1]))) : #queen lies in a common row or column or diag
                return False #fails to satisfy CSP


        index += 1 #increment for next iter

    return True



def backtracking(grid):
    start = time.time()

    solutionCount = 0
    queens = []
    queue = []
    num_queens = len(grid)

    for i in range(0,num_queens): #i can load up queue initially without worry for inconsistent states
            queue.append([str(i)])
    
    
           
    
    while (len(queue) != 0): 
        check = time.time()

        if (check-start > TIME_LIM):
            return -1
        
        path = queue.pop(0)
       
        

        if len(path) == num_queens: #if path length == num queens, we're done
            #solutionCount += 1
            visualizeQueens(path)

            return time.time()-start
        

        #perform initial pruning
        
        neighs = [] #domain for next column (variable assignment)
        for i in range(0,num_queens):
            
            
            if (checkConsistency(path+[str(i)])): #only add to domain of neighboring assignment if it is consistent
                queue.insert(0,path+[str(i)])
        
        if len(neighs) == 0: #we can't add any more valid queens
            #print "pruned all possible positions, backtracking"
            continue #backtrack
        
            
               
               
    return solutionCount
            



#experimentation
times = []
for qs in range(0,100):
    grid = np.zeros([qs,qs])
    t =  backtracking(grid)
    print t
    if (t == -1):
        #plot times and exit
        for rem in range(qs, 100):
            times.append(TIME_LIM)
        plt.plot(times)
        #plt.show()
        np.save("forwardChecking.npy",times)
        exit()

    times.append(t)
