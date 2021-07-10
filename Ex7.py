from math import factorial

def fact(n):
    if n == 1:
        yield 1
    else:
        for i in fact(n - 1):
            yield i
        yield i * n

n = 4
res = fact(n)
for el in res:
    print(el)

print(f'Проверка: {factorial(n)}')