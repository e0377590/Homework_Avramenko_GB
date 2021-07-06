def int_func(my_str):
    return my_str.capitalize()

my_str = input('Введите строку разделенную пробелами: ').split(" ")

for word in my_str:
    print(int_func(word), end = ' ')
