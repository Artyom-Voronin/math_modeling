V0 = float(input())
x0 = float(input())
y0 = float(input())
import numpy as np
import lab3_ex1 as physic
count1 = [0]
count2 = [0]
count3 = [1, 2, 3, 4, 5]
for t in range(1,6):
    c = (x0 + V0*t)
    count1.append(c)
  
for t in range(1,6):
    b = (x0 + V0*t - (physic.g*t**2)/2)
    count2.append(b)
    
A = np.zeros((3, 6))    
for i in range(0,6):
    A[0,i] = i

for n in range(1,6):
    A[1, n] = count1[n]
for n in range(1,6):
    A[2, n] = count2[n]
print(A)    