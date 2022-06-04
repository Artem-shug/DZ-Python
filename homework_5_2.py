# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import deque


def summa(x, y):
    my_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    k = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)
    while x:
        if y:
            res = my_dict[x.pop()] + my_dict[y.pop()] + k
        else:
            res = my_dict[x.pop()] + k
        k = 0
        if res < 16:
            result.appendleft(my_dict[res])
        else:
            result.appendleft(my_dict[res - 16])
            k = 1
    if k:
        result.appendleft('1')
    return list(result)


def multiplication(x, y):
    my_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    xx = deque([deque() for _ in range(len(y))])

    x, y = x.copy(), deque(y)
    for i in range(len(y)):
        m = my_dict[y.pop()]
        for j in range(len(x) - 1, -1, -1):
            xx[i].appendleft(m * my_dict[x[j]])
        for _ in range(i):
            xx[i].append(0)
    k = 0
    for _ in range(len(xx[-1])):
        res = k
        for i in range(len(xx)):
            if xx[i]:
                res += xx[i].pop()
        if res < 16:
            result.appendleft(my_dict[res])
        else:
            result.appendleft(my_dict[res % 16])
            k = res // 16
    if k:
        result.appendleft(my_dict[k])
    return list(result)


a = list(str(input('Введите число: ')).upper())
b = list(str(input('Введите число: ')).upper())
print(a)
print(b)
print('Сумма =', summa(a, b))
print('Произведение =', multiplication(a, b))
