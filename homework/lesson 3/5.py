def my_func(arg):
    my_list = arg.split()
    result = 0
    for i in my_list:
        i = int(i)
        result += i
    return result


res = 0

while True:
    my_input = input('Введите числа разделенные пробелом')
    if my_input == 'q':
        break
    res += my_func(my_input)
    print(res)