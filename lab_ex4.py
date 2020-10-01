a = int(input())
x = 1
y = 2

print(x, y, end=" ")
for i in range(3, a+1):
    print(x+y, end=" ")
    b = x
    x = y
    y = b+x
print()


