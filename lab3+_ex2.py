import numpy as np
arr = np.zeros(5)
print('Заполните массив')
for i in range(4):
     arr[i] = int(input())

print('Введите значение')
ch = int(input())
print('Позицию в массиве')
nmb = int(input())
arr = np.insert(arr, nmb, ch)
arr = np.resize(arr, 5)
print(arr)