# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего
# задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# 1 вариант
from random import randint
from time import perf_counter


n = 10000
a = [randint(100, 10000) for i in range(n)]

# 1 вариант

begin = perf_counter()
b = sorted(a)[:2]
print(b)
end = perf_counter()
print('time ', end - begin)
print()

# 2 вариант

begin = perf_counter()
min1 = min(a)
a.remove(min1)
min2 = min(a)
print(f'{min1}, {min2}')
end = perf_counter()
print('time ', end - begin)
print()

# 3 вариант

begin = perf_counter()
a = []
N = 10000
for i in range(N):
    a.append(randint(100, 10000))

if a[0] > a[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2, N):
    if a[i] < a[min1]:
        b = min1
        min1 = i
        if a[b] < a[min2]:
            min2 = b
    elif a[i] < a[min2]:
        min2 = i

print(f'{a[min1]}, {a[min2]}')
end = perf_counter()
print('time ', end - begin)
