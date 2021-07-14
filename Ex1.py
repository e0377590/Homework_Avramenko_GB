
my_list = []
while True:
    str = input('Введите строку (для окончания введите пустую строку): ')
    if str == '':
        break
    else:
        my_list.append(str + '\n')

f = open('Example1.txt', 'w')
f.writelines(my_list)
f.close()
