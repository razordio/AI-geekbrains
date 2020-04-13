from itertools import count, cycle

start_number = int(input('Введите начальное число: '))
# print []
for i in count(start_number):
  print(i),
  if i > 100:
    break

my_list = [1, 'a', 123]
for j in cycle(my_list):
    print(j)
