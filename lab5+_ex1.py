from sympy.vector import CoordSys3D
from sympy import symbols, solve
from math import acos, degrees

N = CoordSys3D('N')

a = 4*N.i + 3*N.j + 8*N.k
b = -2*N.i + 8*N.j + 7*N.k
c = -5*N.i - 6*N.j + 12*N.k

def v_cos(v1, v2):
    res = v1.dot(v2)/(v1.magnitude()*v2.magnitude())
    return degrees( acos(res.evalf()))
print(v_cos(a,b))
print(v_cos(a,c))
print(v_cos(c,b))

x = symbols('x')

a = 7*N.i + 2*N.j - 8*N.k
b = -4*N.i + x*N.j + 9*N.k

result = solve(a.dot(b), x)
print(result)