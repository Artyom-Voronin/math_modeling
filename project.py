import matplotlib.pyplot as plt
import numpy as np
import constant as cnst

#Вычисляем ускорение свободного падения на планетах
g_Earth = (cnst.G * cnst.M_Earth)/(cnst.R_Earth**2)
g_Mars = (cnst.G * cnst.M_Mars)/(cnst.R_Mars**2)
g_Jupiter = (cnst.G * cnst.M_Jupiter)/(cnst.R_Jupiter**2)

#Вычисляем первую космическую скорость на планетах
V1_Earth = np.sqrt(cnst.G * cnst.M_Earth/cnst.R_Earth)/1000
V1_Mars = np.sqrt(cnst.G * cnst.M_Mars/cnst.R_Mars)/1000
V1_Jupiter = np.sqrt(cnst.G * cnst.M_Jupiter/cnst.R_Jupiter)/1000

#Вычисляем вторую космическую скорость на планетах
V2_Earth = np.sqrt(2*cnst.G * cnst.M_Earth/cnst.R_Earth)/1000
V2_Mars = np.sqrt(2*cnst.G * cnst.M_Mars/cnst.R_Mars)/1000
V2_Jupiter = np.sqrt(2*cnst.G * cnst.M_Jupiter/cnst.R_Jupiter)/1000

def circle1(R = 3,title = "my circle"):
    x = np.arange(-3, 3, 0.1)
    y = np.arange(-3, 3, 0.1)
    x, y = np.meshgrid(x,y)
    fxy = x**2 + y**2
    plt.contour(x, y, fxy, levels=[R])
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)    
    plt.axis("equal")

def circle(R = 2,title = "my circle"):
    x = np.arange(-3, 3, 0.1)
    y = np.arange(-3, 3, 0.1)
    x, y = np.meshgrid(x,y)
    fxy = x**2 + y**2
    plt.contour(x, y, fxy, levels=[R])
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)    
    plt.axis("equal") 
   
def parabola(a=1, title = "Model"):
    x = np.arange(-0.7, 1.1, 0.01)
    y = (x**3)+1.9 
    plt.plot(x, y, color='k')
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)
    plt.plot(x, y, color='k', marker='8', ms=0.4)
    
def sputnik11(R = 0.02,title = "my circle"):
    x = np.arange(-4, 4, 0.1)
    y = np.arange(-4, 4, 0.1)
    x, y = np.meshgrid(x,y)
    fxy = (x-0.5)**2 + (y-2)**2
    plt.contour(x, y, fxy, levels=[R])
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)    
    plt.axis("equal")
    
def sputnik12(R = 0.01,title = "my circle"):
    x = np.arange(-4, 4, 0.1)
    y = np.arange(-4, 4, 0.1)
    x, y = np.meshgrid(x,y)
    fxy = (x-0.5)**2 + (y-2)**2
    plt.contour(x, y, fxy, levels=[R])
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)    
    plt.axis("equal")
    
def sputnik13(R = 0.005,title = "my circle"):
    x = np.arange(-4, 4, 0.1)
    y = np.arange(-4, 4, 0.1)
    x, y = np.meshgrid(x,y)
    fxy = (x-0.5)**2 + (y-2)**2
    plt.contour(x, y, fxy, levels=[R])
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)    
    plt.axis("equal")
sputnik13()   
sputnik12()   
sputnik11()  
circle1()     
parabola()
plt.show() 

def ellipse(a = 3.5, b = 2, title="my ellipse"):
    x = np.arange(-4, 4.1, 0.1)
    y = np.arange(-4, 4.1, 0.1)
    x, y = np.meshgrid(x,y)
    fxy = (x**2)/(a**2) + (y**2)/(b**2)
    plt.contour(x, y, fxy, levels=[1])
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)
    plt.axis("equal")

def sputnik21(R = 0.02,title = "my circle"):
    x = np.arange(-4, 4, 0.1)
    y = np.arange(-4, 4, 0.1)
    x, y = np.meshgrid(x,y)
    fxy = x**2 + (y-2)**2
    plt.contour(x, y, fxy, levels=[R])
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)    
    plt.axis("equal")
    
def sputnik22(R = 0.01,title = "my circle"):
    x = np.arange(-4, 4, 0.1)
    y = np.arange(-4, 4, 0.1)
    x, y = np.meshgrid(x,y)
    fxy = x**2 + (y-2)**2
    plt.contour(x, y, fxy, levels=[R])
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)    
    plt.axis("equal")

sputnik22()    
sputnik21()   
ellipse()
circle()
plt.show() 

def circle2(R = 2,title = "my circle"):
    x = np.arange(-5, 5, 0.1)
    y = np.arange(-5, 5, 0.1)
    x, y = np.meshgrid(x,y)
    fxy = x**2 + y**2
    plt.contour(x, y, fxy, levels=[R])
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)    
    plt.axis("equal")
    

def parabola(a = -2, b = 0, c = 2, title = "my parabola"):
    x = np.arange(-0.6, 0.6, 0.01)
    y = a*x**2 + b*x + c
    
    plt.plot(x, y, color='k')
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)
    
 
def sputnik31(R = 0.02,title = "my circle"):
    x = np.arange(-4, 4, 0.1)
    y = np.arange(-4, 4, 0.1)
    x, y = np.meshgrid(x,y)
    fxy = x**2 + (y-2)**2
    plt.contour(x, y, fxy, levels=[R])
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)    
    plt.axis("equal")
    
def sputnik32(R = 0.01,title = "my circle"):
    x = np.arange(-4, 4, 0.1)
    y = np.arange(-4, 4, 0.1)
    x, y = np.meshgrid(x,y)
    fxy = x**2 + (y-2)**2
    plt.contour(x, y, fxy, levels=[R])
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title(title)    
    plt.axis("equal")
  
sputnik32()    
sputnik31()
parabola()
circle2()
plt.show()
