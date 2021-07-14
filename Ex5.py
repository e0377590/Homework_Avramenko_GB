

from random import randint

number = randint(10, 30) # общее количество чисел в файле
my_str = ''
for i in range(number):
    if i == number - 1:
        my_str += str(randint(0, 1000))
    else:
        my_str += str(randint(0, 1000)) + ' '

with open('Example5.txt', 'w') as f:
    f.write(my_str)
with open('Example5.txt') as f:
    my_str = f.read()
    my_str = my_str.split(' ')
    sum = 0
    for number in my_str:
        sum += int(number)

print(f'Сумма всех чисел в файле: {sum}')