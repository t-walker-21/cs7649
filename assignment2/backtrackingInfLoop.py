import numpy as np
import time
import copy


num_queens = 4

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

def SelectValue(Xi):

    #create a temporary domain to for while loop
    tempDomain = []
    for i in range(0,num_queens):
        tempDomain.append(str(i))

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
    i = 1
    a = ''

    #copy domain of first variable (domain for all vars are the same)
    domain = []
    for d in range(0,num_queens):
        domain.append(str(d))

    #print domain
    x = []

    #print SelectValue('0') 

    while (i >= 1 and i <= num_queens):
        x = SelectValue(a) #add to assignments Ai
        print "i: " , i, " x: " , x
        if x == None: #no value was returned
            i -= 1 #backtrack
            a = a[:-1]

        else: #else step forward
            a += x #add to assignments Ai also?
            i += 1
            #here domain copying isn't really needed since all domains are the same

    if i == 0:
        print "inconsistent"

    else:
        print a


backtracking()