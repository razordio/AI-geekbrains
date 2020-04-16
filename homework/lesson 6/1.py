import time
class TrafficLight:
    def __init__(self, color):
        self.__color = color
    def running(self):
        if self.__color == 'Красный':
            print('Красный')
            time.sleep(7)
            print('Желтый')
            time.sleep(2)
            print('Зеленый')
            time.sleep(2)
            print('')
        elif self.__color == 'Желтый':
            print('Желтый')
            time.sleep(2)
            print('Зеленый')
            time.sleep(2)
        elif self.__color == 'Зеленый':
            print('Зеленый')
            time.sleep(2)


color = input('Введите цвет: ')
a = TrafficLight(color)
a.running()

