from functools import reduce

def reducer_func(el_prev, el):
    # el_prev — предшествующий элемент
    # el — текущий элемент
    return el_prev * el


my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(my_list)

print(reduce(reducer_func, my_list))