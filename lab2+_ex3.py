number = int(input())
number1 = number
i=0
count = []  
while number1 % 10 != 0:
    i = i + 1
    number1 = number1 // 10
for n in range(1, i + 1):
    c = number % 10
    count.append(c)
    number = number // 10  
    
print(*count, sep='')  







