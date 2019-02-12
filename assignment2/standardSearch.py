import numpy as np
import time
import copy
import sys

def checkLen(queens):
    return len(queens.split(','))


def DFS(grid):
  queue = []
  visited = []

  queue.append(startNode)
    
  while len(queue) != 0:
    path = queue.pop(0)
    node = path[-2:]
    print "node", node
    if node == goalNode:
      print "Goal state found. Path is: ", path
      return path, maxQSize
    
      
    #get all edges of current node
    e = g[node]
    e = np.sort(np.array(e))
    print "bordering states-->", e   
      
    for edge in e:
      #print edge
      if not(edge in visited):
        queue.insert(0,path+"-"+edge)
        visited.append(edge)
    
    if not(node in visited):
      visited.append(node)
    print "visited", visited
    print "queue", queue
    if len(queue) > maxQSize:
      maxQSize = len(queue)


def generateNeighbors(state,maxLen):#helper function to generate all possible neighbors of a state
    neighbors = []


    #grid[r][c]

    

    if (state[0] != 0): #there exists a neighbor above this state
        neighbors.append((state[0]-1,state[1]))
        #print "trueUp"

    if (state[0] != maxLen-1): #there exists a neighbor below this state
        neighbors.append((state[0]+1,state[1]))
        #print "trueDown"

    if (state[1] != 0): #there exists a neighbor left of this state
        neighbors.append((state[0],state[1]-1))
        #print "trueLeft"
    
    if (state[1] != maxLen-1): #there exists a neighbor right of this state
        neighbors.append((state[0],state[1]+1))
        #print "trueRight"

    return neighbors

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
            if (n[0] == q[0] or n[1] == q[1] or (abs(n[0] - q[0]) == abs(n[1] - q[1]))) : #queen lies in a common row or column or diag
                return False #fails to satisfy CSP


        index += 1 #increment for next iter

    return True


def standardSearch(grid):

    solutionCount = 0
    queens = []
    queue = []
    visited = []
    #grid[0][0] = 1 #start search at top left (0,0) position
    #state = '0' #this should work better than ^
    assignmentCount = 0 #var to track if all possible vars have been assigned

    for i in range(0,num_queens):
            queue.append(str(i))
    
    
           
    
    while (len(queue) != 0):
        
        path = queue.pop(0)
        #print path

        if (len(path) == num_queens):
            #print "checking: ", path
               
            if checkConsistency(path):
                print "solution found: " , path
                visualizeQueens(path)
                solutionCount += 1
                continue
            else:
                #print "no path found"
                continue
            
            
            
        
        #queens.append(currState)
        #print 'currState', currState
        


        """if (len(queens) == len(grid)): #all queens have been assigned, check constraints to see if these assignments fulfill CSP
            visualizeQueens(queens)

            print "checking consistency"
            queens.pop()
            assignmentCount -= 1

        neighs = generateNeighbors(currState,len(grid))"""
        neighs = []
        for i in range(0,num_queens):
            neighs.append(str(i))
    

        for n in neighs:
            #if not(n in visited):
            queue.insert(0,path+n)
                #visited.append(currState+n)

        #print "queens" , queens
        #print "queue" , queue
        #print path
        
        
        #if not(currState in visited):
            #visited.append(currState)        
    return solutionCount
            


num_queens = int(sys.argv[1])

grid = np.zeros([num_queens,num_queens])

#pieces = '20314'
#print "CSP satisfied? --> ", checkConsistency(pieces)
#visualizeQueens(pieces)
print "found: " , standardSearch(grid), " solutions"