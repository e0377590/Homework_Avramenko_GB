def first_func(num1, num2):
    if num2 == 0:
        print('Деление на ноль!')
    else:
        return num1 / num2

num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))

print(f'Ваш результат : {first_func(num1, num2)}')