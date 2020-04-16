class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_count(self):
        sm = 5
        count_m = self._length * self._width * sm * 25
        print(count_m)

length = int(input('введите длину полотна: '))
width = int(input('введите ширину полотна: '))
mass = Road(length, width)
mass.mass_count()