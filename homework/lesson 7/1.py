class Matrix:
    def __init__(self, matrix):
        self.lists = matrix

    def __elements(self):
        for row in self.lists:
            print(row, end='\n')

    def __add__(self, other):
        for i in range(len(self.lists)):
            for j in range(len(self.lists[i])):
                self.lists[i][j] += other[i][j]
        return Matrix(self.lists)

    def __str__(self):
        return f"{self.__elements()}"


matrix = [[32, 24, 10], [18, 45, 23], [56, 12, 44]]
matrix2 = [[32, 24, 10], [18, 45, 23], [56, 12, 44]]
my_matrix = Matrix(matrix)
my_matrix2 = Matrix(matrix2)

print(my_matrix + matrix2)

