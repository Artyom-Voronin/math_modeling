import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
x = np.arange(-5, 5, 0.01)

def diff_func(n, x):
    y, omega = n
    dy_dt= omega
    dw_dt = np.sin(x)+np.cos(x)
    return dy_dt, dw_dt
    
y0=3
omega=0
n0= y0, omega

sol = odeint(diff_func, n0, x)

plt.plot(x, sol[:, 1], 'b', label='diff')

plt.legend()
plt.show()