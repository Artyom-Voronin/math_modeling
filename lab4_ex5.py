import numpy as np
import math

print("Введите тип фигуры: треугольник, прямоугольник, круг")
shape = input()

def S_rectangle(a=0, b=0):
    a, b = map(int, input().split())
    return a*b
    
def S_triangle(a=0, b=0, c=0):
    a, b, c = map(int, input().split())
    p = (a + b + c) / 2
    S = math.sqrt(p*(p - a)*(p - b)*(p - c))
    return S

def S_circle(r=0):
    r = int(input())
    return np.pi * r**2

def ask_S_figure():
    if shape == "треугольник":
        print("Введите стороны треугольника")
        print(S_triangle())
    elif shape == "прямоугольник":
        print("Введите стороны прямоугольника")
        print(S_rectangle())
    elif shape == "круг":
        print("Введите радиус круга")
        print(S_circle())
    else:
        print("Такой формы нет")
        
ask_S_figure()
    