import numpy as np
import time


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

    if (state[0] != maxLen): #there exists a neighbor below this state
        neighbors.append((state[0]+1,state[1]))
        #print "trueDown"

    if (state[1] != 0): #there exists a neighbor left of this state
        neighbors.append((state[0],state[1]-1))
        #print "trueLeft"
    
    if (state[0] != maxLen): #there exists a neighbor right of this state
        neighbors.append((state[0],state[1]+1))
        #print "trueRight"

    return neighbors

def visualizeQueens(queens):
    tempGrid = np.zeros([len(queens),len(queens)])
    for q in queens:
        tempGrid[q[0]][q[1]] = 1

    print tempGrid
    time.sleep(2)


def standardSearch(grid):

    queens = []
    queue = []
    visited = []
    #grid[0][0] = 1 #start search at top left (0,0) position
    state = (0,0) #this should work better than ^
    assignmentCount = 0 #var to track if all possible vars have been assigned

    queue.append(state)   
    
    while (len(queue) != 0):
        path = queue.pop(0)
        currState = path
        queens.append(currState)
        print currState
        

        assignmentCount += 1 #each time a state is popped from the queue, a queen has been assigned. 

        if (assignmentCount == len(grid)): #all queens have been assigned, check constraints to see if these assignments fulfill CSP
            visualizeQueens(queens)

            print "checking constraints"
            queens.pop()
            assignmentCount -= 1

        neighs = generateNeighbors(currState,len(grid)**2)
        

        for n in neighs:
            if not(n in visited):
                queue.insert(0,n)
                visited.append(n)

        print queens
        
        if not(currState in visited):
            visited.append(currState)        

            


num_queens = 4

grid = np.zeros([num_queens,num_queens])


standardSearch(grid)