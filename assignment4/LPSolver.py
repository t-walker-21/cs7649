import numpy as np
import sys
import time

def rowRed(arr,pivot): #perform row reduction
    if (arr[pivot[0]][pivot[1]] == 1):
        pass

    else:
        arr[pivot[0]] /= arr[pivot[0]][pivot[1]]
    
    counter = 0
    for row in arr:
        if (counter == pivot[0]):
            counter += 1 
            continue
        opp = arr[counter][pivot[1]] * -1
        
        
        arr[counter] = row + arr[pivot[0]] * opp
        counter += 1

    return arr


def calcPivot(arr):
    #find the pivot element
    row = arr[0]
    col = np.argmin(row)

    least = sys.maxint
    counter = 1
    pivot = 0

    for row in arr[1:]:
        if row[col] == 0:
            counter += 1
            continue
        #print row, row[-1]/row[col]
        if row[-1]/row[col] < least and row[-1]/row[col] > 0:
            least = row[-1]/row[col]
            pivot = counter
            #print "least: ", least
            #print counter,col
        counter += 1
    return pivot,col



def calcPivot2(arr): #for minimizing
    #find the pivot element
    row = arr[0]
    tempRow = []
    for r in row:
        if not(r <= 0):
            tempRow.append(r)

    tempRow = np.array(tempRow)
    col = min(tempRow)#np.argmin(row)
    col = np.where(row == col)[0][0]

    least = sys.maxint
    counter = 1
    pivot = 0

    for row in arr[1:]:
        if row[col] == 0:
            counter += 1
            continue
        #print row, row[-1]/row[col]
        if abs(row[-1]/row[col]) < least:
            least = abs(row[-1]/row[col])
            pivot = counter
            #print "least: ", least
            #print counter,col
        counter += 1
    return pivot,col

#arr = np.array([[-3,-5,0,0,0,0],[1,0,1,0,0,4],[0,2,0,1,0,12],[3,2,0,0,1,18]],dtype=np.float32)

#arr = np.array([[3,5,0,0,0,0],[1,0,1,0,0,4],[0,2,0,1,0,12],[3,2,0,0,-1,1]],dtype=np.float32)

#arr = np.array([[3,5,-6,0,0,0,0],[4,10,0,-1,0,0,1],[1,2,7,0,1,0,5],[1,0,1,0,0,-1,1]],dtype=np.float32)

#arr = np.array([[-2,3,0,0,0],[3,4,1,0,24],[7,-4,0,1,16]],dtype=np.float32)

#arr = np.array([[-2,-4,0,0,0],[1,4,1,0,12],[1,3,0,1,10]],dtype=np.float32)

arr = np.array([[-6,-6,0,0,0],[1,3,1,0,2],[2,2,0,1,5]],dtype=np.float32)

#arr = np.array([[3,5,-6,0,0,0,0],[4,0,10,-1,0,0,1],[1,2,7,0,1,0,5],[1,0,1,0,0,-1,1]],dtype=np.float32)

arr = np.array([[-1,-1,-2,0,0,0,0],[2,1,1,1,0,0,50],[2,1,0,0,-1,0,36],[1,0,1,0,0,-1,10]],dtype=np.float32)

print arr

temp = 'f'
prev = None
for _ in range(20):
    time.sleep(5)
    #prev = arr[:][:]
    pivot,col = calcPivot(arr)
    print arr[pivot][col], (pivot,col)
    #exit()
    arr2 = rowRed(arr,(pivot,col))
    print arr2
    arr = arr2[:][:]
    #if (arr2[0][-1] < prev[0][-1]): #check to see if the optimization is complete
        #break


print arr2

