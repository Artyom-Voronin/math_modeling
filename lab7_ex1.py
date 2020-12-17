import matplotlib.pyplot as plt
import numpy as np

t1 = np.arange(-15, 15, 0.1)
R1 = 1

x1 = R1 * (t1 - (np.sin(t1))**3)
y1 = R1 * (1 - (np.cos(t1))**3)

plt.plot(x1, y1, ls='-', lw=3)
plt.axis('equal')
plt.show()

t2= np.arange(-15, 15, 0.1)
R2 = 5

x2 = R2 * (np.cos(t2))**3
y2 = R2 * (np.sin(t2))**3

plt.plot(x2, y2, ls='-', lw=3)
plt.axis('equal')
plt.show()

