# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# 1 вариант через min, max
import random

n = 20
a = [0] * n

for i in range(n):
    a[i] = random.randint(0, 100)
print(a)

min_a = min(a)
max_a = max(a)
i_min_a = a.index(min_a)
i_max_a = a.index(max_a)
print(f'min значение {min_a} = его индекс {i_min_a}, max значение {max_a} = его индекс {i_max_a}')
a[i_min_a], a[i_max_a] = a[i_max_a], a[i_min_a]
print(a)

# 2 вариант
import random

n = 20
a = [0] * n
min_a = 0
max_a = 0
for i in range(n):
    a[i] = random.randint(0, 100)
print(a)
for i in range(n):
    if a[i] < a[min_a]:
        min_a = i
    elif a[i] > a[max_a]:
        max_a = i
print(f'min значение {a[min_a]} = его индекс {min_a}, max значение {a[max_a]} = его индекс {max_a}')
a[min_a], a[max_a] = a[max_a], a[min_a]
print(a)
