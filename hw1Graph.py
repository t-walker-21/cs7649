import numpy as np

vertices = ["AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MO","MN","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VA","VT","WA","WV","WI","WY"]
edges = [["AL","GA"],["AL","FL"],["AL","MS"],["AL","TN"],
["AR","LA"],["AR","TX"],["AR","OK"],["AR","MS"],["AR","MS"],["AR","MO"],
["AZ","CA"],["AZ","NV"],["AZ","UT"],["AZ","NM"],
["CA","OR"],["CA","NV"],["CA","AZ"],
["CO","NM"],["CO","KS"],["CO","UT"],["CO","WY"],["CO","NE"],["CO","OK"],
["CT","RI"],["CT","MA"],["CT","NY"],
["DC","MD"],["DC","VA"],
["DE","NJ"],["DE","PA"],["DE","MD"],
["FL","AL"],["FL","GA"]
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
["MO"],[],[],[],[],[],[],[],
]



print len(vertices)
exit()
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