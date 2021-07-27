
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    inp_data = input("Введите число: ")
    try:
        inp_data = float(inp_data)
        if inp_data == 0:
            raise OwnError("Деление на ноль!")
    except ValueError:
        print("Вы ввели не число!")
    except OwnError as err:
        print(err)
        break
    else:
        print("Все хорошо!")