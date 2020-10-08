a = float(input())
b = float(input())
c = float(input())


if ((a+b) > c) and ((a+c) > b) and ((c+b) > a):
    print('Треугольник существует')
    if (a != b) and (c != b) and (a != c):
        print('Треугольник разносторонний')
    elif ((a == b) and (c != b) and (c != a)) or ((c == b) and (a != b) and (c != a)) or ((a == c) and (a != b) and (c != b)):
        print('Треугольник равнобедренный')
    else:
        print('Треугольник равносторонний')
else: 
    print('Треугольник не существует')
    