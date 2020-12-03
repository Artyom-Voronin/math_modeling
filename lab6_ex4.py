import matplotlib.pyplot as plt
import numpy as np
def logprb(a, b, title = "my logarifmic parabola"):
    f = np.arange(0, 8*np.pi, 0.01) 
    r = a*np.exp(b*f)
    
    rx = r * np.cos (f)
    ry = r * np.sin (f)
    
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)
    plt.axis("equal")
    plt.plot(rx,ry)
    plt.show()
logprb(0.5,0.1)

def archspiral(k, title = "my archimedean spiral"):
    f = np.arange(0, 8*np.pi, 0.01) 
    r = k * f
    
    rx = r * np.cos (f)
    ry = r * np.sin (f)
    
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)
    plt.axis("equal")
    plt.plot(rx,ry)
    plt.show()
archspiral(12)

def spiralwand(k, title = "my spiral wand"):
    f = np.arange(0.01, 8*np.pi, 0.01) 
    r = k / np.sqrt(f)
    
    rx = r * np.cos (f)
    ry = r * np.sin (f)
    
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)
    plt.axis("equal")
    plt.plot(rx,ry)
    plt.show()
spiralwand(12)

def spiralrose(k, title = "my spiral rose"):
    f = np.arange(0.01, 8*np.pi, 0.01) 
    r = np.sin(k*f)
    
    rx = r * np.cos (f)
    ry = r * np.sin (f)
    
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)
    plt.axis("equal")
    plt.plot(rx,ry)
    plt.show()
spiralrose(14)




