import numpy as np
rows = int(input())
columns = int(input())
A = np.zeros((rows, columns))
B = []
for(i,j), x in np.ndenumerate(A):
    A[i,j] = int(input())
x = 0


for m in range(columns):
    for n in range(0, rows):
        if A[n, m] > x:
            x = A[n, m]
    
    B.append(x)



print(A)
print(B)
