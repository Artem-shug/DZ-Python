# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

n = 10
a = []

for i in range(n):
    a.append(int(random.randint(-30, 0)))
print(a)

i = 0
idx = 0
while i < n:
    if a[i] < 0 and idx == 0:
        idx = i
    elif 0 > a[i] > a[idx]:
        idx = i
    i += 1
print(f'значение {a[idx]} на позиции {idx+1}')
