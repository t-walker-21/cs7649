#Tevon Walker CS7649 -- Homework 3B problem 7

#mdp definition

states = [[],[],[],[]]
init_dist = [1,0,0,0]
actions = [0,1]
trans_mat1 = [[0.1,0.9,0,0],[0.9,0.1,0,0],[0,0,0.1,0.9],[0,0,0,1]]
trans_mat2 = [[0.9,0.1,0,0],[0,0.1,0,0.9],[0.9,0,0.1,0],[0,0,0,1]]
reward = [0,0,0,1]
discount_factor = 0.95

#initialize value function

value = [0,0,0,0]

