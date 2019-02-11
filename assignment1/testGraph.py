import numpy as np
import sys
import time

vertices = ["A","B","C","D","E","F","G","H","I"]
edges = [["A","B"],["A","C"],["A","D"],
["B","A"],["B","C"],["B","E"],
["C","A"],["C","B"],
["D","A"],["D","E"],["D","F"],
["E","B"],["E","D"],
["F","D"],["F","G"],
["G","F"],["G","H"],
["H","G"],["H","I"],
["I","H"]
]


"""for vert in vertices:
 for edge in edges:
  if vert == edge[0]:
   print vert,edge"""


def buildGraph(vertices,edges):
 
 g = {}

 for vert in vertices:
  nodes = []
  for edge in edges:
   if vert == edge[0]:
    #print vert,edge
    nodes.append(edge[1])

  g[vert] = nodes
  
 return g

def BFS(g,startNode,goalNode):
 queue = []
 visited = []
 

 queue.append(startNode)
 
 while len(queue) != 0:
  path = queue.pop(0)
  node = path[-2:]
  if node == goalNode:
   print "Goal state found. Path is: ", path 
   return
  print "node", node
  
  #get all edges of current node
  e = g[node]
  e = np.sort(np.array(e))
  print "e", e
  
  for edge in e:
   if not(edge in visited or edge in queue):
    queue.append(path+edge)
    

  visited.append(node)
  print "visited", visited
  print "queue" , queue


def DFS(g,startNode,goalNode):
  
  depth = 1

  while depth < len(vertices):
    print "IDS ITER: " , depth
    print "\n"
    queue = []
    visited = []
    
    queue.append(startNode)
    
    while len(queue) != 0:
      path = queue.pop(0)
      node = path[-1]
      print "node", node
      if node == goalNode:
        print "Goal state found. Path is: ", path
        return
      
      #get all edges of current node
      e = g[node]
      e = np.sort(np.array(e))
      print "e-->", e 
      
      
      for edge in e:
        if not(edge in visited):
          if (len(path.split("-")) + 1 <= depth):
            print "pushing: " , edge
            queue.insert(0,path+"-"+edge)
            visited.append(edge)

      if not(node in visited):
        visited.append(node)
      print "visited", visited
      print "queue", queue
      print "q size-> " , len(queue)


    depth += 1
        

    


g = buildGraph(vertices,edges)


if sys.argv[3] == "b":
 start = time.time()
 BFS(g,sys.argv[1],sys.argv[2])
 end = time.time()
 print end-start, " seconds"

else:
  start = time.time()
  DFS(g,sys.argv[1],sys.argv[2])
  end = time.time()
  print end-start, " seconds"