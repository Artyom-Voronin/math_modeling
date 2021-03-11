import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 5, frames)

def move_func(z, t):
    x, vx, y, vy = z
    dxdt = vx
    dvxdt = 0
    dydt = vy
    dvydt = -((vy / abs(vy)) * mu * vy ** 2 + g)
    return dxdt, dvxdt, dydt, dvydt


g = 9.8
v = 20
m = 0.5
mu = 0.1

x0 = 0
vx0 = 0
y0 = 0
vy0 = v

z0 = x0, vx0, y0, vy0

def solve_func(i):
    sol = odeint(move_func, z0, t)
    x = sol[i, 0]
    y = sol[i, 2]
    return x, y

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')

def animate(i):
    ball.set_data(solve_func(i))


ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

edge = 15
ax.set_xlim(-1, edge)
ax.set_ylim(-1, edge)

plt.show()





	
