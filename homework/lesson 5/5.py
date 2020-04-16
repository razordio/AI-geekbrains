file = open('file_for_5.txt', 'w')
numbers = input('Введите числа через пробел: ')
file.write(numbers)
file.close()
file = open('file_for_5.txt', 'r')

for line in file:
    summ = 0
    n_list = line.split(' ')
    for number in n_list:
        summ += int(number)
print(summ)


