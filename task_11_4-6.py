

class Office_equipment:
    def __init__(self):
        try:
            self.model = input('Введите модель: ')
            self.price = int(input('Введите цену: '))
            self.quantity = int(input('Введите колличество: '))
            if self.price < 0 or self.quantity < 0:
                raise ValueError
        except ValueError:
            print('ДАННЫЕ ВВЕДЕНЫ НЕ ВЕРНО !!!')
    
    def reception(self):
        result = {'модель': self.model, 'цена': self.price, 'колличество': self.quantity}
        print(result)


class Printer(Office_equipment):
    def __init__(self):
        super().__init__()
        try:
            self.cartridge = int(input('Введите колличество картриджей: '))
            if self.cartridge < 0:
                raise ValueError              
        except ValueError:
            print('ДАННЫЕ ВВЕДЕНЫ НЕ ВЕРНО !!!')
        
    def reception(self):
        try:
            result = {'модель': self.model, 'цена': self.price, 'колличество': self.quantity, 'картриджи': self.cartridge}
            print(result)
        except AttributeError:
            print('ДАННЫЕ ВВЕДЕНЫ НЕ ВЕРНО !!!')


class Scanner(Office_equipment):
    def __init__(self):
        super().__init__()
        self.scanning_speed = input('Введите скорость сканирования: ')
    
    def reception(self):
        result = {'модель': self.model, 'цена': self.price, 'колличество': self.quantity, 'скорость сканирования': self.scanning_speed}
        print(result)


class Xerox(Office_equipment):
    def __init__(self):
        super().__init__()
        try:
            self.number_of_copies = int(input('Введите число копий: '))
            if self.number_of_copies < 0:
                raise ValueError
        except ValueError:
            print('ДАННЫЕ ВВЕДЕНЫ НЕ ВЕРНО !!!')
    
    def reception(self):
        try:
            result = {'модель': self.model, 'цена': self.price, 'колличество': self.quantity, 'число копий': self.number_of_copies}
            print(result)
        except AttributeError:
            print('ДАННЫЕ ВВЕДЕНЫ НЕ ВЕРНО !!!')


class Transfer_of_equipment(Office_equipment):
    def __init__(self, department_name):
        super().__init__()
        self.department_name = department_name
        try:
            self.transfer_quantity = int(input('Введите колличество отдаваемой техники: '))
            if self.transfer_quantity < 0:
                raise ValueError
        except ValueError:
            print('ДАННЫЕ ВВЕДЕНЫ НЕ ВЕРНО !!!')

    def transfer(self):
        try:
            res = self.quantity - self.transfer_quantity
            if self.transfer_quantity < 0:
                raise ValueError('ВВЕДЕНО НЕ ПРАВИЛЬНОЕ ЗНАЧЕНИЕ')
            print(f'В {self.department_name} отдали {self.model} в колличестве {res} шт.')
        except AttributeError:
            print('ДАННЫЕ ВВЕДЕНЫ НЕ ВЕРНО !!!')
        except ValueError as error:
            print(error)


a = Office_equipment()
a.reception()
b = Printer()
b.reception()
c = Scanner()
c.reception()
d = Xerox()
d.reception()
e = Transfer_of_equipment('бухгалтерия')
e.transfer()

