def my_func (x, y, z):
    my_list = []
    my_list.append(x)
    my_list.append(y)
    my_list.append(z)
    my_list.sort()
    my_list.reverse()
    return my_list[0] + my_list[1]

a = int(input('Введите параметр №1: '))
b = int(input('Введите параметр №2: '))
c = int(input('Введите параметр №3: '))

print(my_func(a, b, c))
