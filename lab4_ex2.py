import numpy as np
import random as rnd

mass1 = np.array([rnd.randint(1, 11) for i in range(10)])

def muliply_mass(mass):
    result = 1
    for i in mass:
        result *= i
    return result
print(mass1)
print(muliply_mass(mass1))