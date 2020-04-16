file = open("file_for_4.txt", "r")
wr_file = open("wr_file_for_4.txt", "w")
dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
list = []
for line in file:
    list = line.split(' ')
    wr_file.write(dict[list[0]]+ ' ' + list[1] + ' ' + list[2])
wr_file.close()
file.close()