import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw=2)

def circle_expand(R, t):
    r = R * t * 0.05
    alp = np.arange(0, 2 * np.pi + 0.1, 0.1)
    x = r * np.cos(alp)
    y = r * np.sin(alp)
    return x, y

edge = 15
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    anim_object.set_data(circle_expand(R=1, t=i))
    
ani = FuncAnimation(fig,
                    animate,
                    frames=100,
                    interval=30
                    )

ani.save('lec_7_complex_animation.gif')


