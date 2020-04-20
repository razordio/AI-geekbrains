class Car:
    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = False
    def go(self):
        print(f'{self.name} Поехал')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction):
        print(f'{self.name} повернул {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости")
        else:
            print(f'Текущая скорость {self.speed}')

class SportCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        self.show_speed()

    def show_speed(self):
        if self.speed < 100:
            print("Может поднажмем?")
        else:
            print(f'Текущая скорость {self.speed}')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости")
        else:
            print(f'Текущая скорость {self.speed}')


class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        self.is_police = True
        self.__show_police()
    def __show_police(self):
        print("Всем оставаться на своих местах - работает ОМОН")





a = Car("Lexus", 60, "Green")
a.go()
a.show_speed()
a.turn("Left")
a.stop()

b = PoliceCar("Lada", 120, "black")

c = TownCar("WV", 80, "White")
c.show_speed()

d = SportCar("Lycan", 90, "Red")