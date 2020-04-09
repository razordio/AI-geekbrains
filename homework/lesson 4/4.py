import random
import collections

my_list = [random.randint(0,10) for i in range(10)]
print(my_list)

new_list = [item for item, count in collections.Counter(my_list).items() if count == 1]
print(new_list)