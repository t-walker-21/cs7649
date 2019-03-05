#Tevon Walker -- CS7649 Homework 3a - problem 2

trans_matrix = [[0.1,0.4,0.5],[0.4,0,0.6],[0,0.6,0.4]]
sensor_matrix = [[0.5,0.5],[0.9,0.1],[0.1,0.9]]
initial_dist = [1,0,0]
obser_seq = [2,3,3,2,2,2,3,2,3]
obser_dict = {2:0,3:1}

#print trans_matrix
#print sensor_matrix
#print initial_dist
#print obser_seq

delta = [[],[],[]]
pre = [[],[],[]]

#initialize delta and Pre
for s in range(0,len(initial_dist)):
    #print s
    delta[s] = initial_dist[s] * sensor_matrix[s][obser_dict[obser_seq[0]]]
    pre[s] = -1



print delta

for z in range(1,len(obser_seq)-1): #for each observation
    delta_prev = delta[:]
    
    
    
    for s in range(0,len(initial_dist)): #for all states
        maxProd = 0
        for q in range(0,len(initial_dist)): #must find maximum value across all q's
            #print delta_prev
            temp = delta_prev[q]*trans_matrix[q][s]
            if temp > maxProd:
                maxProd = temp
        
        delta[s] = maxProd*sensor_matrix[s][obser_dict[obser_seq[z+1]]]
        
    print delta
    if (z == 2):
        break
