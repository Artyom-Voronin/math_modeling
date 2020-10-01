a = int(input())
b = int(input())
if b == 0 :
    print('На ноль делить нельзя')
elif ((a%b)== 0) and (b>0):
    print('Числа делятся')
    print('Частное =', a//b)
else:
    print('Числа не делятся')
    print('Частное =', a // b)
    print('Остаток =', a%b)