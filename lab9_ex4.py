import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 100, 1)

V_0=0
k=2
b=3000
F= b
m = 100

def speed_function(V, t):
    dfdt = b - k * F*t/m
    return dfdt
    
solve_Bi = odeint(speed_function, V_0, t)

plt.plot(t, solve_Bi[:,0], label='V(t)')
plt.xlabel('Время')
plt.ylabel('Скорость')
plt.title('График движения')
plt.legend()

plt.show()