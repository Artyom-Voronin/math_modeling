number = int(input())
for i in range(1, number+1):
    x = 0
    for k in range(1, i//2 + 1):
        if i % k ==0:
            x += k
    if x == i:
        print(x)
    
    
    
        