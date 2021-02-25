import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
t = np.arange(0, 3, 0.01)

def diff_func(n, t):
    y, omega = n
    dy_dt=omega
    dw_dt=(1 - omega**2)**0.5
    return dy_dt, dw_dt

y0=1
omega = 0
n0= y0, omega
sol = odeint(diff_func, n0, t)

plt.plot(t, sol[:, 0], 'b', label='diff')

plt.legend()
plt.show()