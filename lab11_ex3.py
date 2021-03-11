import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 5, frames)

def move_func(z, t):
    y, vy = z
    dydt = vy
    dvydt = - k * y / m - g
    return dydt, dvydt

g = 9.8
m = 0.5
v0 = 0.5
k = 12.5
y0 = -0.08

z0 = y0, v0

def solve_func(i):
    sol = odeint(move_func, z0, t)
    x = 0
    y = sol[i, 0]
    return x, y

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')

def animate(i):
    ball.set_data(solve_func(i))


ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

edge = 1
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()
