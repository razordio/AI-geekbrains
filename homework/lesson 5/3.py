file = open("file_for_3.txt", "r")
# employee_dict = {}
lines = 0
summ = 0
for line in file:
    lines += 1
    list = []
    list = line.split(' ')
    if int(list[1]) >= 20000:
        print(list[0])
    summ += int(list[1])
print(summ / lines)
file.close()