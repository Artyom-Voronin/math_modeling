import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 

frames = 100000
time = 0.1
t = np.linspace(0, time, frames)
def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3,
     x4, v_x4, y4, v_y4,
     x5, v_x5, y5, v_y5,
     x6, v_x6, y6, v_y6) = s

    dxdt1 = v_x1
    dv_xdt1 = k * Q * q  * x1 /m * (x1**2 + y1**2)**1.5
    dydt1 = v_y1
    dv_ydt1 = k * Q * q * y1 /m * (x1**2 + y1**2)**1.5

    dxdt2 = v_x2
    dv_xdt2 = k * Q * q * x2 /m * (x2**2 + y2**2)**1.5
    dydt2 = v_y2
    dv_ydt2 = k * Q * q * y2 /m * (x2**2 + y2**2)**1.5
    
    dxdt3 = v_x3
    dv_xdt3 = k * Q * q  * x3 /m * (x3**2 + y3**2)**1.5
    dydt3 = v_y3
    dv_ydt3 = k * Q * q  * y3 /m * (x3**2 + y3**2)**1.5
    
    dxdt4 = v_x4
    dv_xdt4 = - k * Q * q  * x4 /m * (x4**2 + y4**2)**1.5
    dydt4 = v_y4
    dv_ydt4 = - k * Q * q  * y4 /m * (x4**2 + y4**2)**1.5
    
    dxdt5 = v_x5
    dv_xdt5 = - k * Q * q  * x5 /m * (x5**2 + y5**2)**1.5
    dydt5 = v_y5
    dv_ydt5 = - k * Q * q  * y5 /m * (x5**2 + y5**2)**1.5
    
    dxdt6 = v_x6
    dv_xdt6 = - k * Q * q  * x6 /m * (x6**2 + y6**2)**1.5
    dydt6 = v_y6
    dv_ydt6 = - k * Q * q  * y6 /m * (x6**2 + y6**2)**1.5

    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3,
            dxdt4, dv_xdt4, dydt4, dv_ydt4,
            dxdt5, dv_xdt5, dydt5, dv_ydt5,
            dxdt6, dv_xdt6, dydt6, dv_ydt6)
k = 9 * 10**9
Q=500
q=7
m=0.01

x10 = 10000
v_x10 = -50
y10 = 1000
v_y10 = -4

x20 = 6500
v_x20 = -30
y20 = 4000
v_y20 = -10

x30 = 3500
v_x30 = -15  
y30 = 10000
v_y30 = -8

x40 = -3500
v_x40 = 27  
y40 = 12000
v_y40 = 3

x50 = -6500
v_x50 = 40  
y50 = 4200
v_y50 = 4

x60 = -1000
v_x60 = 7  
y60 = 2000
v_y60 = 0

s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60)
def solve_func(i, key):
    sol = odeint(move_func, s0, t)
    if key == 'point':
        x1 = sol[i, 0]
        y1 = sol[i, 2]
        x2 = sol[i, 4]
        y2 = sol[i, 6]
        x3 = sol[i, 8]
        y3 = sol[i, 10]
        x4 = sol[i, 12]
        y4 = sol[i, 14]
        x5 = sol[i, 16]
        y5 = sol[i, 18]
        x6 = sol[i, 20]
        y6 = sol[i, 22]
        
    else:
        x1 = sol[:i, 0]
        y1 = sol[:i, 2]
        x2 = sol[:i, 4]
        y2 = sol[:i, 6]
        x3 = sol[:i, 8]
        y3 = sol[:i, 10]
        x4 = sol[:i, 12]
        y4 = sol[:i, 14]
        x5 = sol[:i, 16]
        y5 = sol[:i, 18]
        x6 = sol[:i, 20]
        y6 = sol[:i, 22]
    return ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6))
fig, ax = plt.subplots()

ball1, = plt.plot([], [], 'o', color='r')

ball2, = plt.plot([], [], 'o', color='r')

ball3, = plt.plot([], [], 'o', color='r')

ball4, = plt.plot([], [], 'o', color='b')

ball5, = plt.plot([], [], 'o', color='b')

ball6, = plt.plot([], [], 'o', color='b')

plt.plot([0], [0], 'o', color='k', ms=15)

def animate(i):
    ball1.set_data(solve_func(i, 'point')[0])    

    ball2.set_data(solve_func(i, 'point')[1])    
    
    ball3.set_data(solve_func(i, 'point')[2])    
    
    ball4.set_data(solve_func(i, 'point')[3])    
    
    ball5.set_data(solve_func(i, 'point')[4])    
    
    ball6.set_data(solve_func(i, 'point')[5])    
    
ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

plt.axis('equal')
edge = 2*x10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()





