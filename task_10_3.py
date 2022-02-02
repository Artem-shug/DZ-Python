

class Cell:
    def __init__(self, number):
        self.number = int(number)

    def __add__(self, other):
        return self.number + other.number
    
    def __sub__(self, other):
        if self.number - other.number > 0:
            return self.number - other.number
        else:
            return 'Разница меньше нуля'

    def __mul__(self, other):
        return self.number * other.number
    
    def __floordiv__(self, other):
        return self.number // other.number

    def make_order(self, size):
        sizes = ['*' * size for i in range(self.number // size)]
        res = '*' * (self.number % size)
        sizes.append(res)
        return '\n'.join(sizes)
              

cell_1 = Cell(20)
cell_2 = Cell(7)

print(cell_1.__add__(cell_2))
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)

print(cell_1.make_order(6))


