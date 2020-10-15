V0 = float(input())
x0 = float(input())
y0 = float(input())
import numpy as np
import lab3_ex1 as physic
count1 = []
count2 = []
count3 = [1, 2, 3, 4, 5]
for t in range(1,6):
    c = (x0 + V0*t)
    count1.append(c)
  
for t in range(1,6):
    b = (x0 + V0*t - (physic.g*t**2)/2)
    count2.append(c)
12
print('t', *count3, sep='    ')
print('x', count1)
print('y', count2)