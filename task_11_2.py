

class My_Zero(Exception):
    def __init__(self, txt):
        self.txt = txt
while True:
    try:
        param_1 = int(input('Введите делимое: '))
        param_2 = int(input('Введите делитель: '))

        if param_2 == 0:
            raise My_Zero('Делить на ноль нельзя')
        else:
            result = param_1 / param_2
    
    except ValueError:
        print('Вы ввели не число')
        print()
    except My_Zero as error:
        print(error)
        print()
    else:
        print(result)
        print()

