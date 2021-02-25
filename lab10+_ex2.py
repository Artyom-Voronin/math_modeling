import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
x = np.arange(0, 5, 0.01)

def diff_func(n, x):
    y, omega = n
    dx_dy=omega
    dw_dx= (omega**2 - (3*y**2)/x**0.5)/y   
    return dx_dy, dw_dx

y0=0.01
omega = 1
n0= y0, omega
sol = odeint(diff_func, n0, x)

plt.plot(x, sol[:, 0], 'b', label='diff')

plt.legend()
plt.show()