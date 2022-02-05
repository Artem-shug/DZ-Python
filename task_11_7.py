

class Complex_number:
    def __init__(self, num_1, num_2):
        self.num_1 = int(num_1)
        self.num_2 = int(num_2)
    
    def __str__(self):
        return f'({self.num_1}+{self.num_2}j)'
    
    def __add__(self, other):
        return Complex_number(self.num_1 + other.num_1, self.num_2 + other.num_2)
    
    def __mul__(self, other):
        new_num_1 = self.num_1 * other.num_1 - self.num_2 * other.num_2
        new_num_2 = self.num_1 * other.num_2 + self.num_2 * other.num_1
        return Complex_number(new_num_1, new_num_2) 


a = Complex_number(1, 2)
b = Complex_number(3, 4)

print(a + b)
print(a * b)

