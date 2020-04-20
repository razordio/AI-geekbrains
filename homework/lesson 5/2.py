file = open("file_for_2.txt")

lines = 0
line_number = 1
for line in file:
    lines += 1
    words_in_line = line.count(' ')

    print(f'Слов в строке {line_number} - {words_in_line + 1}')
    line_number += 1

print("Lines:", lines)
file.close()