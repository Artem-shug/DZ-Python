

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')
        print()


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} - Отрисовка синим цветом')
        print()


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} - Отрисовка серым цветом')
        print()


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} - Отрисовка черным цветом')
        print()


stationery = Stationery('')
stationery.draw()

pen = Pen('ручка')
pen.draw()

pencil = Pencil('карандаш')
pencil.draw()

handle = Handle('маркер')
handle.draw()

