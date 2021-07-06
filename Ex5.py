def my_func():
    my_list = []
    amount = 0
    while True:
        my_str = input('Введите числа разделенные пробелом или введите Q для окончания: ')
        if my_str.count('Q') == 0:
            my_list = list(map(int, my_str.split(" ")))
            amount += sum(my_list)
            print(f'Сумма введенных чисел {amount}')
        else:
            if my_str.index('Q') == 0:
                print(f'Сумма введенных чисел {amount}')
                return amount
            my_str = my_str[:my_str.index('Q') - 1]
            my_list = list(map(int, my_str.split(" ")))
            amount += sum(my_list)
            print(f'Сумма введенных чисел {amount}')
            return amount

amount = my_func()
