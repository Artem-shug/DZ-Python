# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

n = int(input())
max_sum = 0
max_num = 0
while n != 0:
    m = n
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    if s > max_sum:
        max_sum = s
        max_num = m
    n = int(input())
print('Число',max_num,'имеет максимальную сумму цифр:', max_sum)