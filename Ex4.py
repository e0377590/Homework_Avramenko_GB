def my_pow1(x, y):
    return x ** y

def my_pow2(x, y):
    num = 1 / x
    res = 1

    for i in range(abs(y)):
        res *= num
    return res

num1 = float(input('Введите первое число: '))
num2 = int(input('Введите второе целое отрицательное число: '))

print(f'Первый вариант: {my_pow1(num1, num2)}')
print(f'Второй вариант: {my_pow2(num1, num2)}')
print(f'Проверка: {pow(num1, num2)}')