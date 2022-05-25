# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# 1 вариант
import random

n = 10
a = [random.randint(1, 50) for i in range(n)]
print(a)

b = sorted(a)[:2]
print(b)

# 2 вариант
import random

n = 10
a = [random.randint(1, 50) for i in range(n)]
print(a)

min1 = min(a)
a.remove(min1)
min2 = min(a)
print(f'{min1}, {min2}')
