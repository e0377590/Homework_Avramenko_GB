
f = open('Example4_1.txt', 'r')
my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []

for i, line in enumerate(f):
    line = line.split(' ', 1)
    line[0] = my_dict[line[0]]
    my_list.append(line[0] + ' ' + line[1])
f.close()

with open('Example4_2.txt', 'w', encoding='utf-8') as f:
    f.writelines(my_list)
