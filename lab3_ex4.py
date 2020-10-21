import numpy as np
N = 3
M = 4
ar = []
for i in range(N):
    a = []
    for j in range(M):
        a.append(np.sin(N*(i+1) + M*(j+1)))
    ar.append(a)
print(ar)     
 
for i in range(N):
    for j in range(M):
        if ar[i][j] < 0:
            ar[i][j] = 0
print(ar)         
      