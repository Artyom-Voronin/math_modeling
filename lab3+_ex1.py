import numpy as np
rows = int(input())
columns = int(input())
A = np.zeros((rows, columns))
B = np.zeros((rows, columns))
C = np.zeros((rows, columns))


for(i,j), x in np.ndenumerate(A):
    A[i,j] = int(input())
    
for(i,j), x in np.ndenumerate(B):
    B[i,j] = int(input())
    
print(A) 
print(B)
for(i,j), x in np.ndenumerate(C):
    if A[i,j] > B[i,j]:
        C[i,j] = A[i,j]
    else:
        C[i,j] = B[i,j]
print(C)