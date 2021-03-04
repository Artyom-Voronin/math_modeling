import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
frames = 200
t = np.linspace(0, 5, frames)

def move_func(z, t):
    x, y = z
    dxdt = k1 * (A - x - y)
    dydt = k2 * (A - x - y)
    return dxdt, dydt
A=50
k1=5
k2=1.2

x0 = 0
y0 = 0

z0 = x0, y0

def solve_func(i, key):
    sol = odeint(move_func, z0, t)
    if key == 'point':
        x = t[i]
        y = sol[i, 1]
    else:
        x = t[:i]
        y = sol[:i, 1]
    return x, y
    
fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')
def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))
    
ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

edge = 70
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

plt.show()                  