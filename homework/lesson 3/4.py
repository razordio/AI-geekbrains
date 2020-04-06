def my_func(x, y):
    res = x ** y
    return res


def my_func_1(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y >= 0:
        return result
    else:
        return 1 / result


x = int(input('Введите число для возведения в степень: '))
y = int(input('Введите степень возведения: '))

print('Результат варианта 1: {}'.format(my_func(x, y)))
print('Результат варианта 2: {}'.format(my_func_1(x, y)))