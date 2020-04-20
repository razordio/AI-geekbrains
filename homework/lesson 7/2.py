class Clothes:
    def __init__(self, type1):
        self.name = type1


class Coat(Clothes):
    def __init__(self, v, type1):
        super().__init__(type1)
        self.len = v

    @property
    def cloth(self):
        cloth = self.len / 6.5 + 0.5
        return cloth


class Costume(Clothes):
    def __init__(self, h, type1):
        super().__init__(type1)
        self.len = h

    @property
    def cloth(self):
        cloth = self.len * 2 + 0.3
        return cloth


c = Coat(150, "Пальто")
j = Costume(200, "Костюм")
print(f"Для одежды типа: {c.name} нужно {c.cloth}м ткани")
print(f"Для одежды типа: {j.name} нужно {j.cloth}м ткани")
print(f"Итого нужно {c.cloth + j.cloth}м ткани")
