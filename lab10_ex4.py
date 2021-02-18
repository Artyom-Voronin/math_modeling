import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
t = np.arange(-5, 5, 0.01)

def diff_func(n, t):
    y, omega = n
    dy_dt= omega
    dw_dt = -4 *omega - 5*y
    return dy_dt, dw_dt
    
y0=4
omega=-1
n0= y0, omega

sol = odeint(diff_func, n0, t)

plt.plot(t, sol[:, 1], 'b', label='diff')

plt.legend()
plt.show()