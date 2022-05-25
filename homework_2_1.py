# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о
# невозможности деления на ноль, если он ввел 0 в качестве делителя.

while True:
    a = input('Введите знак операции: ')
    if a == '0':
        print('цикл завершен')
        break
    if a == '+' or a == '-' or a == '*' or a == '/':
        try:
            b = float(input('Введите 1 число: '))
            c = float(input('Введите 2 число: '))
        except ValueError as v:
            print('ВВЕДИТЕ ЧИСЛО !!!')
        else:
            if a == '+':
                print(b + c)
            elif a == '-':
                print(b - c)
            elif a == '*':
                print(b * c)
            elif a == '/':
                if c == 0:
                    print('Делить на 0 нельзя')
                else:
                    print(b / c)
    else:
        print('Введен не верный знак операции')
        print()
