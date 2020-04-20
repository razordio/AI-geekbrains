class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other)

    def __sub__(self, other):
        if self.cells < other:
            print("Маловата еще для вычитания")
            return Cell(self.cells)
        else:
            return Cell(self.cells - other)

    def __mul__(self, other):
        return Cell(self.cells * other)

    def __truediv__(self, other):
        return Cell(self.cells // other)

    def make_order(self, other):
        for i in range(self.cells // other):
            cells = ''
            for j in range(other):
                cells += '*'
            print(cells)
        for i in range(self.cells % other):
            print('*', end='')

new_cell = Cell(12)
new_cell += 5
new_cell -= 18
new_cell *= 2
new_cell /= 2
new_cell.make_order(5)