class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []

while True:
    inp_data = input("Введите число (для окончания программы введите stop): ")
    if inp_data == 'stop':
        break
    try:
        if inp_data.isdigit() == False:
            raise OwnError("В вашем элементе списка присутствуют не только числа!")
    except OwnError as err:
        print(err)
    else:
        my_list.append(int(inp_data))

print(my_list)