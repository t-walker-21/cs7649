import numpy as np
import sys
import time

vertices = ["AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MO","MN","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VA","VT","WA","WV","WI","WY"]
edges = [["AL","GA"],["AL","FL"],["AL","MS"],["AL","TN"],
["AR","LA"],["AR","TX"],["AR","OK"],["AR","MS"],["AR","MS"],["AR","MO"],
["AZ","CA"],["AZ","NV"],["AZ","UT"],["AZ","NM"],
["CA","OR"],["CA","NV"],["CA","AZ"],
["CO","NM"],["CO","KS"],["CO","UT"],["CO","WY"],["CO","NE"],["CO","OK"],
["CT","RI"],["CT","MA"],["CT","NY"],
["DC","MD"],["DC","VA"],
["DE","NJ"],["DE","PA"],["DE","MD"],
["FL","AL"],["FL","GA"],
["GA","AL"],["GA","FL"],["GA","TN"],["GA","NC"],["GA","SC"],
["IA","NE"],["IA","SD"],["IA","MN"],["IA","WI"],["IA","IL"],["IA","MO"],
["ID","OR"],["ID","WA"],["ID","MT"],["ID","WY"],["ID","UT"],["ID","NV"],
["IL","IA"],["IL","WI"],["IL","IN"],["IL","KY"],["IL","MO"],
["IN","IL"],["IN","MI"],["IN","OH"],["IN","KY"],
["KS","CO"],["KS","NE"],["KS","MO"],["KS","OK"],
["KY","MO"],["KY","IL"],["KY","IN"],["KY","OH"],["KY","WV"],["KY","WV"],["KY","TN"],
["LA","TX"],["LA","AR"],["LA","MS"],
["MA","NY"],["MA","VT"],["MA","NH"],["MA","RI"],["MA","CT"],
["MD","WV"],["MD","PA"],["MD","DE"],["MD","DC"],["MD","VA"],
["ME","NH"],
["MI","WI"],["MI","OH"],["MI","IN"],
["MO","KS"],["MO","NE"],["MS","AL"],
["MT","ND"],["MT","SD"],["MT","WY"],["MT","ID"],
["NC","GA"],["NC","TN"],["NC","VA"],["NC","SC"],
["ND","MN"],["ND","SD"],["ND","MT"],
["NE","WY"],["NE","SD"],["NE","IA"],["NE","MO"],["NE","KS"],["NE","CO"],
["NH","VT"],["NH","ME"],["NH","MA"],
["NJ","PA"],["NJ","NY"],["NJ","DE"],
["NM","AZ"],["NM","CO"],["NM","OK"],["NM","TX"],
["NV","CA"],["NV","OR"],["NV","ID"],["NV","UT"],["NV","AZ"],
["NY","VT"],["NY","MA"],["NY","CT"],["NY","NJ"],["NY","PA"],
["OH","IN"],["OH","MI"],["OH","PA"],["OH","WV"],["OH","KY"],
["OK","NM"],["OK","CO"],["OK","KS"],["OK","MO"],["OK","AR"],["OK","TX"],
["OR","WA"],["OR","ID"],["OR","NV"],["OR","CA"],
["PA","OH"],["PA","NY"],["PA","NJ"],["PA","DE"],["PA","MD"],["PA","WV"],
["RI","CT"],["RI","MA"],
["SC","GA"],["SC","NC"],
["SD","MT"],["SD","ND"],["SD","MN"],["SD","IA"],["SD","NE"],["SD","WY"],
["TN","AR"],["TN","MO"],["TN","KY"],["TN","VA"],["TN","NC"],["TN","GA"],["TN","AL"],["TN","MS"],
["TX","NM"],["TX","OK"],["TX","AR"],["TX","LA"],
["UT","NV"],["UT","ID"],["UT","WY"],["UT","CO"],["UT","AZ"],
["VA","TN"],["VA","KY"],["VA","WV"],["VA","MD"],["VA","DC"],["VA","NC"],
["VT","NH"],["VT","MA"],["VT","NY"],
["WA","OR"],["WA","ID"],
["WV","KY"],["WV","OH"],["WV","PA"],["WV","MD"],["WV","VA"],
["WI","MN"],["WI","MI"],["WI","IL"],["WI","IA"],
["WY","ID"],["WY","MT"],["WY","SD"],["WY","NE"],["WY","CO"],["WY","UT"],
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
  print "bordering states-->", e 
  
  for edge in e:
   if not(edge in visited):
    queue.append(path+"-"+edge)
    visited.append(edge)
    
  if not(node in visited):
    visited.append(node)
  print "visited", visited
  print "queue" , queue

def IDS(g,startNode,goalNode):
  
  depth = 1

  while depth < len(vertices):
    print "IDS ITER: " , depth
    print "\n"
    queue = []
    visited = []
    
    queue.append(startNode)
    
    while len(queue) != 0:
      path = queue.pop(0)
      node = path[-2:]
      print "node", node
      if node == goalNode:
        print "Goal state found. Path is: ", path
        return
      
      #get all edges of current node
      e = g[node]
      e = np.sort(np.array(e))
      print "bordering states-->", e 
      
      
      for edge in e:
        if not(edge in visited):
          if (len(path.split("-")) + 1 <= depth):
            print "pushing: " , edge
            queue.insert(0,path+"-"+edge)
            visited.append(edge)
          else:
            print "Would have added" , edge, "but... reached this iteration's depth limit: " , depth

      if not(node in visited):
        visited.append(node)
      print "visited", visited
      print "queue", queue
      print "q size-> " , len(queue)


    depth += 1

def DFS(g,startNode,goalNode):
  queue = []
  visited = []
  
  queue.append(startNode)
    
  while len(queue) != 0:
    path = queue.pop(0)
    node = path[-2:]
    print "node", node
    if node == goalNode:
      print "Goal state found. Path is: ", path
      return
    
      
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

g = buildGraph(vertices,edges)


if sys.argv[3] == "b":
 start = time.time()
 BFS(g,sys.argv[1],sys.argv[2])
 end = time.time()
 print end-start, " seconds"

elif sys.argv[3] == "d":
  start = time.time()
  DFS(g,sys.argv[1],sys.argv[2])
  end = time.time()
  print end-start, " seconds"

else:
  start = time.time()
  IDS(g,sys.argv[1],sys.argv[2])
  end = time.time()
  print end-start, " seconds"