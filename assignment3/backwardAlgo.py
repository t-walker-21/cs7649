#Tevon Walker -- CS7649 Homework 3b - problem 1A

#HMM
trans_matrix = [[0.1,0.4,0.5],[0.4,0,0.6],[0,0.6,0.4]]
sensor_matrix = [[0.2,0.2,0.2],[0.6,0.6,0.2],[0.2,0.2,0.6]]
initial_dist = [1,0,0]
obser_seq = [1,3,3]
obser_dict = {1:0,2:1,3:2}

#beta algorithm

#compute beta_one

beta = [1,1,1]

for s in range(len(initial_dist)-1,1):
    beta[s] = initial_dist[s]*sensor_matrix[s][obser_dict[obser_seq[0]]]
    
print beta
