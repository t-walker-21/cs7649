#Tevon Walker CS7649 -- Homework 3B problem 7

#mdp definition
import matplotlib.pyplot as plt

states = [[],[],[],[]]
init_dist = [1,0,0,0]
actions = [0,1]
trans_mat1 = [[0.1,0.9,0,0],[0.9,0.1,0,0],[0,0,0.1,0.9],[0,0,0,1]]
trans_mat2 = [[0.9,0.1,0,0],[0,0.1,0,0.9],[0.9,0,0.1,0],[0,0,0,1]]
reward = [0,0,0,1]
discount_factor = 0.5

#initialize value function

value = [0,0,0,0]

horiz = 20

vals1 = []
vals2 = []
vals3 = []
vals4 = []

for h in range(0,horiz): #finite horizion of 100
    
    for s in range(0,len(init_dist)):
        tempMax = float('-inf') # technically, in an mdp, there can exists negative reward, so initialize temp at large neg value
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
        if (s == 0):
            vals1.append(tempMax)
        
        if (s == 1):
            vals2.append(tempMax)

        if (s == 2):
            vals3.append(tempMax)

        if (s == 3):
            vals4.append(tempMax)

    print value

plt.plot(vals1,label='s1')
plt.plot(vals2,label='s2')
plt.plot(vals3,label='s3')
plt.plot(vals4,label='s4')
plt.title('Value of each state as a function of iterations of Value Iterations. Eps = 0.5')
plt.xlabel("Iterations")
plt.ylabel("Value of State")

plt.legend(loc='upper left')

plt.show()