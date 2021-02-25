import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
x = np.arange(-0.99999, 1, 0.01)

def diff_func(n, x):
    y, w = n
    dy_dx=w
    dw_dx=((3*x*w) -a*(a+2)*y)/(1-x**2) 
    return dy_dx, dw_dx

y0=3
w0 = 0
n0= y0, w0
for i in range(2,7):
    a=i
    sol = odeint(diff_func, n0, x)
    plt.plot(x, sol[:, 0], 'b')

plt.legend()
plt.show()