# 4. Определить, какое число в массиве встречается чаще всего.

import random

n = 30
a = [0] * n

for i in range(n):
    a[i] = random.randint(10, 20)
print(a)

number = a[0]
max_count = 1
for i in range(n-1):
    count = 1
    for j in range(i + 1, n):
        if a[i] == a[j]:
            count += 1
        if count > max_count:
            max_count = count
            number = a[i]
if max_count > 1:
    print(f'Число {number} встречаеться {max_count} раз')
else:
    print('Нет встречающихся чисел')
