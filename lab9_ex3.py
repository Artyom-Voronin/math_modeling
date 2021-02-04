import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.1)
a=5
V_0=0
k=0.5
m=5
def speed_function(V, t):
    dvdt = a - ((V**2) * k)/m
    return dvdt
    
solve_Bi = odeint(speed_function, V_0, t)

plt.plot(t, solve_Bi[:,0], label='V(t)')
plt.xlabel('Время')
plt.ylabel('Скорость')
plt.title('График движения')
plt.legend()

plt.show()