#Tevon Walker CS7649 -- Homework 3B problem 7

#mdp definition
import matplotlib.pyplot as plt

states = [[],[],[],[]]
init_dist = [1,0,0,0]
actions = [0,1]
trans_mat1 = [[0.1,0.9,0,0],[0.9,0.1,0,0],[0,0,0.1,0.9],[0,0,0,1]]
trans_mat2 = [[0.9,0.1,0,0],[0,0.1,0,0.9],[0.9,0,0.1,0],[0,0,0,1]]
reward = [0,0,0,1]
discount_factor = 0.95

#initialize value function

value = [0,0,0,0]

horiz = 10

vals1 = [0]
vals2 = [0]
vals3 = [0]
vals4 = [0]

for h in range(0,horiz): #finite horizion of 100
    
    for s in range(0,len(init_dist)): #loop over states
        tempMax = float('-inf') # technically, in an mdp, there can exists negative reward, so initialize temp at large neg value
        value_prev = value[:] #store previous value function
        for a in actions: #must find max value w.r.t action
            total = 0
            for q in range(0,len(init_dist)): #must sum over future states
                if (a == 0): #must apply corresponding transition matrix for an action
                    total += trans_mat1[s][q]*(reward[q] + pow(discount_factor,1)*value_prev[q])
                else:
                    total += trans_mat2[s][q]*(reward[q] + pow(discount_factor,1)*value_prev[q])
            
            if total > tempMax: #select max value across all action
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


for t in range(0,len(vals1)):
    vals1[t] /= (vals4[t] + 1e-5) 
    vals2[t] /= (vals4[t] + 1e-5)
    vals3[t] /= (vals4[t] + 1e-5)
    vals4[t] /= (vals4[t] + 1e-5)

print (vals4[-1])
print (vals3[-1])
print (vals2[-1])
print (vals1[-1])

plt.plot(vals1,label='s1')
plt.plot(vals2,label='s2')
plt.plot(vals3,label='s3')
plt.plot(vals4,label='s4')
plt.title('Value of each state as a function of iterations of Value Iterations. Eps = 0.5')
plt.xlabel("Iterations")
plt.ylabel("Value of State")

plt.legend(loc='lower right')

plt.show()