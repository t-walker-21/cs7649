import numpy as np
import time
import copy #make copies of domains
import sys
from matplotlib import pyplot as plt

TIME_LIM = 10 * 60 

def checkLen(queens): #how long is the current solution?
    return len(queens.split(','))


def visualizeQueens(queens): #visualization function for debugging rules
    tempGrid = np.zeros([len(queens),len(queens)])
    
    count = 0
    for q in queens:
        tempGrid[int(q)][count] = 1
        count += 1
    
    print tempGrid

def checkConsistency(queens): #encorce consistency
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

        
        #check same row and diagonal
        for n in tempList:
            if (n[1] == q[1] or (abs(n[0] - q[0]) == abs(n[1] - q[1]))) : #queen lies in a common row or column or diag
                return False #fails to satisfy CSP


        index += 1 #increment for next iter

    return True


def standardSearch(grid): #algo
    start = time.time()
    num_queens = len(grid) #create grid

    solutionCount = 0
    queens = []
    queue = []
    
        
    #start search at top left (0,0) position
    for i in range(0,num_queens):
            queue.append([str(i)])
    
    
           
    
    while (len(queue) != 0):

        timeNow = time.time()
        if (timeNow-start > TIME_LIM):
            print "time limit: " , TIME_LIM , " exceeded"
            return -1 # -1 denotes time limit has been reached
        
        path = queue.pop(0)
        #enqueue path (queen positions)

        if (len(path) == num_queens): #then check is path is valid
            
               
            if checkConsistency(path): # checking for validity
                print "solution found: " , path
                end = time.time()
                #print end-start, " seconds"
                visualizeQueens(path)
                
                return end-start
                
            else:
                #keep searching
                continue
            
            

        
        neighs = [] #loading up domain for next variable
        for i in range(0,num_queens):
            neighs.append([str(i)])
    

        for n in neighs: #place in queue depth-first style
            queue.insert(0,path+n)
                

        
    return solutionCount
            





#pieces = '20314'
#print "CSP satisfied? --> ", checkConsistency(pieces)
#visualizeQueens(pieces)


#perform experiment
times = []
for qs in range(0,100):
    grid = np.zeros([qs,qs])
    t =  standardSearch(grid)
    print t
    if (t == -1):
        #plot times and exit
        for rem in range(qs, 100):
            times.append(TIME_LIM)
        plt.plot(times)
        #plt.show()
        np.save("standardSearch.npy",times) #save data
        exit()

    times.append(t)



