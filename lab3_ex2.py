import numpy as np
import lab3_ex1 as physic
h = 100
a = np.pi/3
ch = (physic.g * h) * ((np.tan(np.radians(physic.β))**2))
zn1 = 2 * (np.cos(a))**2 
zn2 = 1 - (np.tan(np.radians(physic.β)) * (np.tan(a)))
zn= zn1 * zn2
d = ch/zn
print(np.sqrt(d))
