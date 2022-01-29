

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    
    def massa(self, asphalt, thickness):
        self.asphalt = asphalt
        self.thickness = thickness
        result = (self._length * self._width * self.asphalt * self.thickness)//1000
        print(f'{result} т.')

a = Road(20, 5000)
a.massa(25, 5)

