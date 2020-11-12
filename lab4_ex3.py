import numpy as np
import random as rnd

def full_energy(m, h, v):
    e_kin = (m * v**2)/2
    e_potential = m * 9,8 * h
    return e_kin + e_potential