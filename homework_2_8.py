# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

n = input('Введите последовательность чисел: ')
s = input('Введите цифру: ')

count = 0
for i in n:
    if i == s:
        count += 1
print(f'В веденной последовательности чисел {n} цифра {s} присутствует {count} раз(а)')
