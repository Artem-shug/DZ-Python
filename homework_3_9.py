# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

M = 5
N = 4
a = []
for i in range(N):
    b = []
    for j in range(M):
        x = int(random.randint(1, 100))
        b.append(x)
    a.append(b)
for i in a:
    print(i)

mx = 0
for j in range(M):
    mn = 100
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print('максимальный элемент среди минимальных элементов', mx)
