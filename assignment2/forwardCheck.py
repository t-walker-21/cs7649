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
    visited = []
    checkCount = 0
    #grid[0][0] = 1 #start search at top left (0,0) position
    #state = '0' #this should work better than ^
    assignmentCount = 0 #var to track if all possible vars have been assigned
    num_queens = len(grid)

    for i in range(0,num_queens):
            queue.append([str(i)])
    
    
           
    
    while (len(queue) != 0):
        check = time.time()

        if (check-start > TIME_LIM):
            return -1
        
        path = queue.pop(0)
        #print "path: ", path
        

        if len(path) == num_queens:
            #solutionCount += 1
            visualizeQueens(path)

            return time.time()-start
        #print "checking: ", path

        #perform initial pruning


        
        before = len(queue)
        neighs = [] #domain for next column
        for i in range(0,num_queens):
            
            checkCount += 1
            if (checkConsistency(path+[str(i)])): #only add to domain of neighboring assignment if it is consistent
                #neighs.append([str(i)])
                queue.insert(0,path+[str(i)])
        
        if len(queue) != before:
            continue
        #if len(neighs) == 0: #we can't add any more valid queens
            #print "pruned all possible positions, backtracking"
            #continue #backtrack
        
            
    

        #for n in neighs:
            #if not(n in visited):
            #queue.insert(0,path+n)

        #print "queue" , queue
        #print "prepruned " , num_queens - len(neighs) , " queens"
               
           
            
            
        
        #queens.append(currState)
        #print 'currState', currState

        
        
                #visited.append(currState+n)

        #print "queens" , queens
        #print "queue" , queue
        #print path
        
        
        #if not(currState in visited):
            #visited.append(currState)        
    return solutionCount
            




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
