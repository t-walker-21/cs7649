#Tevon Walker CS7649 -- Homework 3B problem 7

#mdp definition

states = [[],[],[],[]]
init_dist = [1,0,0,0]
actions = [0,1]
trans_mat1 = [[0.1,0.9,0,0],[0.9,0.1,0,0],[0,0,0.1,0.9],[0,0,0,1]]
trans_mat2 = [[0.9,0.1,0,0],[0,0.1,0,0.9],[0.9,0,0.1,0],[0,0,0,1]]
reward = [0,1,0,10]
discount_factor = 0.95

#initialize value function

value = [0,0,0,0]

horiz = 1000


for h in range(0,horiz): #finite horizion of 100
    for s in range(0,len(init_dist)):
        tempMax = -1E11 # technically, in an mdp, there can exists negative reward, so initialize temp at large neg value
        value_prev = value[:]
        for a in actions: #must find max value w.r.t action
            total = 0
            for q in range(0,len(init_dist)): #must sum over future states
                if (a == 0): #must apply correct transition matrix
                    total += trans_mat1[s][q]*(reward[s] + discount_factor*value_prev[q])
                else:
                    total += trans_mat2[s][q]*(reward[s] + discount_factor*value_prev[q])
            if total > tempMax:
                tempMax = total
        
        value[s] = tempMax

    print value

