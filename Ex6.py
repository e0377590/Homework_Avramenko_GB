
with open('Example6.txt', encoding='utf-8') as f:
    result = f.readlines()

result[0] = result[0].replace('\ufeff', '')
my_dict = {}

for subject in result:
    subject = subject.split(':')
    key = subject[0]
    value = 0
    subject[1] = subject[1].replace('(', ' ')
    my_list = subject[1].split(' ')
    for el in my_list:
        if el.isdigit() == True:
            value += int(el)
    my_dict[key] = value

print(my_dict)
