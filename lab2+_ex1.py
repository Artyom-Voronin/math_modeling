a = int(input())
b = int(input())
c = int(input())
d = (b**2)-4*a*c
if d < 0:
    print('Корней нет')
elif d == 0:  
    x = -b/2*a
    print('Единственный корень', x)
else:
    x1 = (-b + d**(1/2))/2*a 
    x2 = (-b - d**(1/2))/2*a   
    print('Первый корень', x1)    
    print('Второй корень', x2)    