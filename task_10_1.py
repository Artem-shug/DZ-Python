

class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
       for i in self.matrix_list:
           print()
           return '\n'.join(map(str, self.matrix_list))
       
    def __add__(self, other):
        for i in range (len(self.matrix_list)):
            for x in range(len(other.matrix_list[i])):
                self.matrix_list[i][x] = self.matrix_list[i][x] + other.matrix_list[i][x]
                if len(self.matrix_list) != len(other.matrix_list):
                    quit('Нельзя складывать матрицы')
                elif len(self.matrix_list[i]) != len(other.matrix_list[i]):
                    quit('Нельзя складывать матрицы')

        return Matrix.__str__(self)
   

matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
matrix_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
matrix_4 = Matrix([[31, 22, 57], [37, 43, 64], [51, 86, -25]])

print(matrix_1.matrix_list)
print(matrix_2.matrix_list)
print(matrix_3.matrix_list)
print(matrix_4.matrix_list)

print(matrix_1)
print(matrix_2)
print(matrix_3)
print(matrix_4)

print(matrix_2 + matrix_4)

