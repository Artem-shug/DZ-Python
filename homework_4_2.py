# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.


from time import perf_counter


# Без использования «Решета Эратосфена»

begin = perf_counter()
n = 10**4
for i in range(2, n):
    simple = True
    for j in range(2, i):
        if i % j == 0:
            simple = False
            break
    if simple:
        print(i, end=', ')
print()
end = perf_counter()
print('time:', end - begin)

# Используя алгоритм «Решето Эратосфена»

begin = perf_counter()
a = [i for i in range(n)]

a[1] = 0
m = 2
while m < len(a):
    if m != 0:
        j = m*2
        while j < len(a):
            a[j] = 0
            j += m
    m += 1
b = [i for i in a if i > 0]
print(b)
end = perf_counter()
print('time:', end - begin)
