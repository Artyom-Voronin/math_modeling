import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

frames = 200
t = np.linspace(0, 5, frames)

def move_func(n, t):
    x, y, z = n
    dxdt = k1 * -x
    dydt = k2 * -y + k1 * x
    dzdt = k3 * -z + k2 * y
    return dxdt, dydt, dzdt

a = 20
k1 = a / 8
k2 = a / 16
k3 = a / 32

x0 = 40
y0 = 0
z0 = 0

n0 = x0, y0, z0

sol = odeint(move_func, n0, t)

fig, ax = plt.subplots()
plt.plot(sol)


plt.grid()
plt.show()