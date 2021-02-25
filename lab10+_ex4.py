import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
x = np.arange(-1, 1, 0.01)

def diff_func(n, x):
    y, w = n
    dy_dx=w
    dw_dx=((y*4*(x**2) + y/2)- x * w)/x**2
    return dy_dx, dw_dx

y0=3
w0 = 0
n0= y0, w0
sol = odeint(diff_func, n0, x)

plt.plot(x, sol[:, 0], 'b', label='diff')

plt.legend()
plt.show()