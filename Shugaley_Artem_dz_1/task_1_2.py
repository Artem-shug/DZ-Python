
numbers = [number ** 3 for number in range(1, 1001, 2)]
numbers_1 = []


count = 0

for i in numbers:
    summ = 0
    a = i
    while i != 0:
        summ += i % 10
        i = i // 10
    if summ % 7 == 0:
        count = count + a
        numbers_1.append(count)
print(sum(numbers_1))


numbers_2 = [number ** 3 + 17 for number in range(1, 1001, 2)]
numbers_3 = []


for i in numbers_2:
    summ = 0
    a = i
    while i != 0:
        summ += i % 10
        i = i // 10
    if summ % 7 == 0:
        count = count + a
        numbers_3.append(count)
print(sum(numbers_3))