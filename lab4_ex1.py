import numpy as np
import random as rnd
mass1 = [rnd.randint(1, 10) for i in range(10)]
def mean_of_mass(mass):
    return(np.mean(mass))
print(mean_of_mass(mass1))