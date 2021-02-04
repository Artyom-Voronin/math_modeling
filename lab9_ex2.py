import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 48, 1)
k = 0.08
n_0 = 1000
def invest_function(n, t):
    dmdt = - k * n * t
    return dmdt
    
solve_Bi = odeint(invest_function, n_0, t)

plt.plot(t, solve_Bi[:,0], label='Инвестиции')
plt.xlabel('Время')
plt.ylabel('Денежные средства')
plt.title('Инвестиции предприятия')
plt.legend()

plt.show()