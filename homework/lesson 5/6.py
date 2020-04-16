import re

file = open("file_for_6.txt", "r")
lessons_dict = {}

for line in file:
    subj = re.split('[:]', line)
    hours = 0
    all_hours = re.findall('(\d+)', subj[1])
    for hour in all_hours:
        hours += int(hour)
    lessons_dict[subj[0]] = hours
print(lessons_dict)
file.close()