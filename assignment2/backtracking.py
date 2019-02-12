import numpy as np
import time
import copy
import sys


num_queens = int(sys.argv[1])

def checkConsistency(queens): #this is the function I made to implement "consistent" in lecture_6.pdf - slide 35
    #enumerate queen coordinates
    queenCoords = []
    count = 0
    for q in queens:
        queenCoords.append((count,int(q)))
        count += 1
    #print queenCoords

    #check constraints for each queen coordinate
    
    index = 0
    
    for q in queenCoords:
        #print "checking -->" , q
        tempList = copy.copy(queenCoords)
        tempList.remove(tempList[index]) #first make a list of coordinates without the queen we're checking
        #print tempList

        
        #check same row and column and diagonal
        for n in tempList:
            if (n[0] == q[0] or n[1] == q[1] or (abs(n[0] - q[0]) == abs(n[1] - q[1]))) : #queen lies in a common row or column or diag
                return False #fails to satisfy CSP


        index += 1 #increment for next iter

    return True


def visualizeQueens(queens):
    tempGrid = np.zeros([len(queens),len(queens)])
    
    count = 0
    for q in queens:
        tempGrid[int(q)][count] = 1
        count += 1
    
    print tempGrid


def SelectValue(Xi,domain):

    #create a temporary domain to for while loop
    tempDomain = copy.copy(domain)

    while (len(tempDomain) != 0): #while domain D'i is not empty
        a = tempDomain.pop(0) #select an arbitrary element a E D'i and remove from D'i
        print "checking consistency of: " , a , "against: ", Xi
        if (checkConsistency(Xi+a)): #if consistent(Ai-1, Xi=a)
            print a , " consistent with: " , Xi
            return a
    return None #no consistent value


#backtracking for N-queens implemented as in the lecture slides on canvas
def backtracking():
    #initialize variable counter, assignments
    i = 0
    a = ''

    #copy domain of first variable (domain for all vars are the same)
    domain = []
    for d in range(0,num_queens):
        domain.append(str(d))

    allDomains = copy.copy(domain) # a copy for restoration

    domains = []
    for d in range(0,num_queens):
        domains.append(copy.copy(domain)) #must shallow copy, else all domains get modified uniformly

    

    #print domain
    x = []

    #print SelectValue('0') 

    while (i >= 0 and i < num_queens):
        print "loop top i: ", i,  " domain: " , domains[i]
        x = SelectValue(a,domains[i]) #add to assignments Ai
        print "i: " , i, " x: " , x 

        if x == None: #no value was returned
            print "inconsistent exhausted, backtracking and removing " , a[-1]
            domains[i-1].remove(a[-1]) #this assignment lead to an inconsistency, remove it from Domain Di to prevent algo from looping infinitely. 
            for j in range(i,len(domains)): #must restore domains because we'll try again at a different assignment
                domains[j] = copy.copy(allDomains)
            i -= 1 #backtrack
            a = a[:-1]
            

        else: #else step forward
            a += x #add to assignments Ai also?
            i += 1
            #here domain copying isn't really needed since all domains are the same

    if i == -1:
        print "inconsistent"

    else:
        print a
        visualizeQueens(a)


backtracking()