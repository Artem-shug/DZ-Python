

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name.capitalize()
            
    @abstractmethod
    def abstract_method(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def consumption(self):
        return f'{self.name} {self.size/6.5 + 0.5} метров'
    
    def abstract_method(self):
        return 'Абстрактный метод для пальто'


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def consumption(self):
        return f'{self.name} {2 * self.height + 0.3} метров'
    
    def abstract_method(self):
        return 'Абстрактный метод для костюма'
        


class All_cloth:
    def __init__(self, size, height):
        self.size = size
        self.height = height
    
    @property
    def all_consumption(self):
        return f'Общий расход ткани {(self.size/6.5 + 0.5) + (2 * self.height + 0.3)} метров'



a = Suit('синий костюм', 1.8)
print(a.consumption)
print(a.abstract_method())

b = Coat('серое пальто', 52)
print(b.consumption)
print(b.abstract_method())

c = All_cloth(52, 1.8)
print(c.all_consumption)

