n = int(input())
mass = []
def fib(n):
    fib1 = fib2 = 1

    if n < 2:
        quit()

    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        mass.append(fib2)
        
if n > 0:
    fib(n)
    print(mass[-1])
elif n < 0:
    fib(-n)
    print(-(mass[-1]))