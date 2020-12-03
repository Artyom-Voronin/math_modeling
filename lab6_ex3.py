import matplotlib.pyplot as plt
import numpy as np

def circle(R = 1,title = "my circle"):
    x = np.arange(-2, 2, 0.1)
    y = np.arange(-2, 2, 0.1)
    x, y = np.meshgrid(x,y)
    fxy = x**2 + y**2
    plt.contour(x, y, fxy, levels=[R])
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)
    plt.axis("equal")
    plt.show()

def ellipse(a = 2, b = 1, title="my ellipse"):
    x = np.arange(-2, 2, 0.1)
    y = np.arange(-2, 2, 0.1)
    x, y = np.meshgrid(x,y)
    fxy = (x**2)/(a**2) + (y**2)/(b**2)
    plt.contour(x, y, fxy, levels=[1])
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)
    plt.axis("equal")
    plt.show()
    
circle()
ellipse()