import json

with open('Example7.txt') as f:
    firm = f.readlines()

num = len(firm)
aver = 0
my_list = []
my_dict = {}

for i, el in enumerate(firm):
    el = el.split()
    income = int(el[2]) - int(el[3])
    if income > 0:
        aver += income
    my_dict[el[0]] = income

my_list.append(my_dict)
my_dict = {}
my_dict['Average profit'] = aver / num
my_list.append(my_dict)

with open('firms.jon', 'w') as f:
    json_firms = json.dump(my_list, f)