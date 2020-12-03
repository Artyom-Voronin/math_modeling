import matplotlib.pyplot as plt
import numpy as np

def parabola(a = 1, b = 1, c = 0, title = "my parabola"):
    x = np.arange(-10, 10, 0.01)
    y = a*x**2 + b*x + c
    
    plt.plot(x, y, color='k')
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)
    plt.grid()
    plt.show()

def hyperbola(n = 1, title="my hyperbola"):
    x = np.arange(-10, 10, 0.01)
    y = n/x
    y = np.ma.masked_less(y, -10)
    y = np.ma.masked_greater(y, 10)
    
    plt.plot(x, y, color='k')
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)
    plt.grid()
    plt.show()
    
parabola()
hyperbola()