import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.01)
k = 2
n_0 = 2
def radio_function(n, t):
    dmdt = k * n
    return dmdt
    
solve_Bi = odeint(radio_function, n_0, t)

plt.plot(t, solve_Bi[:,0], label='Размножение бактерий')
plt.xlabel('Время')
plt.ylabel('Количество бактерий')
plt.title('Размножение бактерий')
plt.legend()

plt.show()