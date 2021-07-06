def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort()
    return my_list[-2] + my_list[-1]

num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
num3 = float(input('Введите третье число: '))

print(f'Ваш результат: {my_func(num1, num2, num3)}')