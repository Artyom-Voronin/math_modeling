import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
x = np.arange(-5, 5, 0.01)

def diff_func(n, x):
    y, z = n
    dy_dx=(y**2)*z
    dz_dx = (z/x)-y*(z**2)
    return dy_dx, dz_dx

y0=1
z0=-3
n0= y0, z0
sol = odeint(diff_func, n0, x)

plt.plot(x, sol[:, 1], 'b', label='diff')

plt.legend()
plt.show()