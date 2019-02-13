import numpy as np
import time
import copy
import sys
from matplotlib import pyplot as plt
TIME_LIM = 10 * 60  


def checkLen(queens): #check solution size
    return len(queens.split(','))


def visualizeQueens(queens): #debug visualization
    tempGrid = np.zeros([len(queens),len(queens)])
    
    count = 0
    for q in queens:
        tempGrid[int(q)][count] = 1
        count += 1
    
    print tempGrid




def checkConsistency(queens): #check valid queen placement
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
   
    neighs = []
    num_queens = len(grid)
    for i in range(0,num_queens):
        neighs.append([str(i)])
        queue.append([str(i)])

    
    
    
           
    
    while (len(queue) != 0):

        if (time.time() - start > TIME_LIM):
            return -1
        
        path = queue.pop(0) #first get a new position

               
        
        if checkConsistency(path): #then check for consistency as in lecture slides (map color example)
            
            if len(path) == num_queens: #if path size is number of queens, we're done
                
                visualizeQueens(path)
                #solutionCount += 1
                return time.time() - start
            
        else: #backtrack
            continue
            
        
            
            
            
    
            

        for n in neighs:
            queue.insert(0,path+n)
                      
    return solutionCount
            


#perform experiment
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
        np.save("backtracking.npy",times)
        exit()

    times.append(t)