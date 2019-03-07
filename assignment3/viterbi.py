#Tevon Walker -- CS7649 Homework 3a - problem 2
import numpy as np

trans_matrix = [[0.1,0.4,0.5],[0.4,0,0.6],[0,0.6,0.4]]
sensor_matrix = [[0.5,0.5],[0.9,0.1],[0.1,0.9]]
initial_dist = [0,0,1]
obser_seq = [1,1,1,2,2,2,1,2,2,1]
obser_dict = {1:0,2:1}

#print trans_matrix
#print sensor_matrix
#print initial_dist
#print obser_seq

delta = [[],[],[]]
pre = [[],[],[]]

#initialize delta and Pre
for s in range(0,len(initial_dist)):
    #print s
    #print delta
    delta[s] = initial_dist[s] * sensor_matrix[s][obser_dict[obser_seq[0]]]
    pre[s] = -1



#print delta
#print pre
Pres = []


for z in range(0,len(obser_seq)-1): #for each observation
    delta_prev = delta[:]
    
    for s in range(0,len(initial_dist)): #for all states
        maxProd = 0
        for q in range(0,len(initial_dist)): #must find maximum value across all q's
            #print "delta_prev",  delta_prev
            temp = delta_prev[q]*trans_matrix[q][s]
            if temp > maxProd:
                maxProd = temp
            
        #print "maxProd" , maxProd * 0.2
        #print sensor_matrix[obser_dict[obser_seq[z+1]]][s]
        delta[s] = maxProd*sensor_matrix[s][obser_dict[obser_seq[z+1]]]
        
        tempList = []
        for q in range(0,len(initial_dist)):
            tempList.append((delta_prev[q]*trans_matrix[q][s]))

        pre[s] = np.argmax(np.array(tempList)) 
    
    #print pre[:]
    Pres.append(pre[:])

        
    #print delta, "delta"
#print Pres , "pre"







#select the most likely state
MLS = np.argmax(np.array(delta))
print max(np.array(delta))
#print MLS, "\n"

path = [[],[],[],[],[],[],[],[],[],[]]
path[-1] = MLS
#print path

#now backtrack to find most likely path

#print Pres[1][MLS]

for z in range(len(obser_seq)-2,-1,-1):
    path[z] =  Pres[(z+1-1)][path[z+1]]




for s in range(0,len(path)):
    path[s] = path[s]+1 

print (np.array(path))
