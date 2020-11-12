import numpy as np
N = 3
M = 3
ar = []
for i in range(N):
    a = []
    for j in range(M):
        a.append(np.sin(N*(i+1) + M*(j+1)))
    ar.append(a)
 
 
for i in range(N):
    for j in range(M):
        if ar[i][j] < 0:
            ar[i][j] = 0
print(ar)
x = 0         
for i in range(N):
    for j in range(M):
        if j == 0 :
            x=ar[i][j]
            ar[i][j]=ar[i][j+1]
            ar[i][j+1]=x
print(ar)

    

