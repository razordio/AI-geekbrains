def my_del(x, y):
    return x / y

my_x = int(input('Введите числитель: '))
my_y = int(input('Введите знаменатель: '))

if my_y == 0:
    print('Деление на 0 запрещено!')
    my_y = int(input('Введите знаменатель: '))

print(my_del(my_x, my_y))