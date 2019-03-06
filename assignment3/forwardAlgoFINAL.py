#Tevon Walker -- CS7649 Homework 3b - problem 1A
import numpy as np

#HMM
trans_matrix = [[0.4,0.6],[0.7,0.3]]
sensor_matrix = [[0.1,0.2,0.1,0.1,0.1,0.2,0.1,0.1],[0.1,0.1,0.2,0.1,0.1,0.1,0.1,0.2]]
initial_dist = [0.8,0.2]
obser_seq = [1,2,3,4,5,6,7,8,3,4,5]
obser_dict = {1:0,2:1,3:2,4:3,5:4,6:5,7:6,8:7}

#forward algorithm

#compute alpha_one

alpha = [[],[]]

#initialize alpha
for s in range(0,len(initial_dist)):
    alpha[s] = initial_dist[s]*sensor_matrix[s][obser_dict[obser_seq[0]]]

print alpha


#compute alphas
for z in range(0,len(obser_seq)-1): #for each observation in the sequence...
    alpha_prev = alpha[:] #make a copy of alpha vector from previous iteration
    #print alpha_prev
    
    for s in range(0,len(initial_dist)): #loop over states s
        total = 0 #sum for sigma term
        for q in range(0,len(initial_dist)): #loop over states we can possibly transition to
            total += alpha_prev[q]*trans_matrix[q][s]
        
        alpha[s] = sensor_matrix[s][obser_dict[obser_seq[z+1]]] * total

    print alpha

print "probability of Z given HMM: " + str (np.array(alpha).sum())
