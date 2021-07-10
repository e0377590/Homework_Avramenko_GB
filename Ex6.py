from itertools import count
from itertools import cycle
from sys import argv

#script_name, first_param = argv

# for el in count(int(first_param)):
#     if el > 15:
#         break
#     else:
#         print(el)

script_name = argv
my_list = ['Anna', 'Victor', 'Tatiana', 'Yury']

с = 0
for el in cycle(my_list):
    if с > 15:
        break
    print(el)
    с += 1