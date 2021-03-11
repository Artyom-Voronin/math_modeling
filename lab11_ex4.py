import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
frames = 200
t = np.linspace(0, 5, frames)

def move_func(z, t):
    m, v, y= z
    dm_dt = -Rt
    dv_dt = ((Vg * Rt)/m)- g
    dv_xdt =v    
    return dv_xdt, dv_dt, dm_dt
    
g=9.8
Vg=3000
m0=250000
Rt=1000
V0=0
y0=0
z0 = m0, V0, y0 

sol = odeint(move_func, z0, t)
plt.plot(t, sol[:, 1], 'r')

plt.show()









