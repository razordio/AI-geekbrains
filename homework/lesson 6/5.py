class Stationery:
    def __init__(self, title=None):
        self.title = title
        self.draw()
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Пишем ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Чертим карандашем")


class Handle(Stationery):
    def draw(self):
        print("Рисуем в лифте :р")

a = Stationery()
b = Pen()
c = Pencil()
d = Handle()
