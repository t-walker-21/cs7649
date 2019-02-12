import numpy as np
import time



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
        tempList = queenCoords.remove(index) #first make a list of coordinates without the queen we're checking

        #check same row
        



def standardSearch(grid):

    queens = []
    queue = []
    visited = []
    #grid[0][0] = 1 #start search at top left (0,0) position
    state = '0' #this should work better than ^
    assignmentCount = 0 #var to track if all possible vars have been assigned

    queue.append('0')
    queue.append('1')
    queue.append('2')
    queue.append('3')
       
    
    while (len(queue) != 0):
        
        path = queue.pop(0)
        print path

        if (len(path) == num_queens):
            print "checking: ", path
            visualizeQueens(path)
            time.sleep(5)
            continue
        
        #queens.append(currState)
        #print 'currState', currState
        


        """if (len(queens) == len(grid)): #all queens have been assigned, check constraints to see if these assignments fulfill CSP
            visualizeQueens(queens)

            print "checking consistency"
            queens.pop()
            assignmentCount -= 1

        neighs = generateNeighbors(currState,len(grid))"""
        neighs = ['0','1','2','3']

        for n in neighs:
            #if not(n in visited):
            queue.insert(0,path+n)
                #visited.append(currState+n)

        #print "queens" , queens
        print "queue" , queue
        time.sleep(3)
        #if not(currState in visited):
            #visited.append(currState)        

            


num_queens = 4

grid = np.zeros([num_queens,num_queens])

pieces = '0023'
checkConsistency(pieces)
visualizeQueens(pieces)
#standardSearch(grid)