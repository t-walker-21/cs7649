import numpy as np

vertices = ["AL","GA","FL","MS","SC","NC","LA","VA","TN","KY"]
edges = [["AL","GA"],["AL","FL"],["AL","MS"],["AL","TN"],["GA","AL"],["GA","FL"],["GA","TN"],["GA","NC"],["GA","SC"]]




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
  node = queue.pop(0)
  if node == goalNode:
   print "goal node found", visited
   return
  print "node", node
  
  #get all edges of current node
  e = g[node]
  e = np.sort(np.array(e))
  print "e", e
  
  for edge in e:
   if not(edge in visited):
    queue.append(edge)
    

  visited.append(node)
  print "visited", visited
  print "queue" , queue


def DFS(g,startNode,goalNode):
  queue = []
  visited = []
  
  queue.append(startNode)
    
  while len(queue) != 0:
    node = queue.pop(0)
    if node == goalNode:
      print "goal node found", visited
      return
    print "node", node
      
    #get all edges of current node
    e = g[node]
    e = np.sort(np.array(e))
      
      
    for edge in e:
      if not(edge in visited):
        queue.insert(0,edge)

    visited.append(node)
    print "visited", visited


g = buildGraph(vertices,edges)
BFS(g,"AL","SC")