class Worker:
    def __init__(self):
        self.name = 'Иван'
        self.surname = 'Петров'
        self.position = 'Директор'
        self._income = {
            'wage': 250000,
            'bonus':  30000
        }

class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')
    def get_total_income(self):
        total_income = int(self._income['wage']) + int(self._income['bonus'])
        print(f'{self.position} получает {total_income}тр')

a = Position()
a.get_full_name()
a.get_total_income()