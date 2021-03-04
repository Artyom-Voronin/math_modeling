import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 5, frames)

def move_func(z, t):
    x, v_x, y, v_y = z
    dxdt = v_x
    dv_xdt = 0
    dydt = v_y
    dv_ydt = - g - k * v 
    return dxdt, dv_xdt, dydt, dv_ydt
g = 9.8
v = 20
k = 0.1
μ = 0.1
alpha = 90 * np.pi / 180

x0 = 0
v_x0 = 0
y0 = 0
v_y0 = v * np.sin(alpha)

z0 = x0, v_x0, y0, v_y0

sol = odeint(move_func, z0, t)

def solve_func(i, key):
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y
  

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='k')
ball_line, = plt.plot([], [], '-', color='k')

def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

ax.set_xlim(-3, 3)
ax.set_ylim(0, 30)

plt.show()







	