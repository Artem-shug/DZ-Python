# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

n = 10
a = []

for i in range(n):
    a.append(int(random.randint(0, 50)))
print(a)

i_min_a = a.index(min(a)) + 1
i_max_a = a.index(max(a)) + 1
print('индекс минимального элемента', i_min_a)
print('индекс максимального элемента', i_max_a)

if i_min_a > i_max_a:
    i_min_a, i_max_a = i_max_a, i_min_a

sum = 0
for i in range(i_min_a + 1, i_max_a):
    sum = sum + a[i]
print('Сумма элементов = ', sum)
