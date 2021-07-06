def print_data(**kwarg):
    str = ('Имя : ', 'Фамилия: ', 'Год рождения: ', 'Город проживания: ', 'Email: ', 'Телефон: ')
    i = 0
    result = ''

    for value in kwarg.values():
        result += str[i] + value + ' '
        i += 1
    print(result)

fields = (('name', 'Имя'), ('surname', 'Фамилия'), ('year', 'год рождения'), ('city', 'город проживания'),
          ('email', 'ваш email'), ('phone', 'телефон'))

data = {}
for field in fields:
    data[field[0]] = input(f'Введите значение поля {field[1]}: ')

print_data(**data)