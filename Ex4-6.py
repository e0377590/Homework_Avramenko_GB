
class Sklad:

    account = 0

    def __init__(self):
        self.dict = {}

    def __str__(self):
        my_str = ''
        for el in self.dict:
            my_str += el + '\n' + '\n'.join(map(str, self.dict[el])) + '\n'
        return my_str

    def add_to_sklad(self, equipment, number):
        try:
            self.account += number
        except TypeError:
            print('Количество товаров на складе задоно не верно')
            return
        my_list = self.dict.setdefault(equipment.name, [])
        my_list.append([equipment.model, equipment.price, number])
      #  self.account += number

    def take_from_sklad(self, equipment, number):
        result = self.dict.get(equipment.name)
        if result == None:
            print('Такого оборудования нет на складе!')
        else:
            try:
                number += 0
            except:
                print('Количество товаров на складе задоно не верно')
                return self
            flag = True
            for i, elem in enumerate(result):
                if elem[0] == equipment.model:
                    flag = False
                    if number < elem[2]:
                        self.account -= number
                        self.dict.get(equipment.name)[i][2] = self.dict.get(equipment.name)[i][2] - number
                        print(f'Товар {equipment.model} отправлен по назначению')
                    elif number == elem[2]:
                        self.account -= number
                        self.dict.get(equipment.name).remove(elem)
                        if len(result) == 0:
                            del self.dict[equipment.name]

                        print(f'Товар {equipment.model} отправлен по назначению')
                    else:
                        print('Количество запрашиваемого товара больше, чем есть на складе')
            if flag == True:
                print('Такого товара нет на складе')
        return self

class Equipment:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price

    def __str__(self):
        return self.name + ' ' + self.model + ' ' + str(self.price)

    def run(self):
        my_str = self.name + ' ' + self.model
        print(f'Устройство {my_str} работает')

class Scaner(Equipment):
    def __init__(self, name, model, price, type, format, speed):
        super().__init__(name, model, price)
        self.type = type
        self.format = format
        self.speed = speed

    @staticmethod
    def scan():
        print('Сканер запустился')

    @staticmethod
    def user_input(self):
        self.name = 'Сканер'
        self.model = input(f'Введите модель сканера: ')
        self.type = input(f'Введите тип сканера: ')
        self.format = input(f'Введите формат(например, А4): ')
        try:
            self.price = int(input(f'Введите цену товара: '))
            self.speed = int(input(f'Введите скорость печати: '))
        except:
            print('Вы ввели не число!')
            return None
        return self


class Printer(Equipment):
    def __init__(self, name, model, price, type, color):
        super().__init__(name, model, price)
        self.type = type
        self.format = format
        self.color = color

    @staticmethod
    def user_input(self):
        self.name = 'Принтер'
        self.model = input(f'Введите модель принтера: ')
        self.type = input(f'Введите тип принтера: ')
        self.color = input(f'Введите цвет печати: ')
        try:
            self.price = int(input(f'Введите цену товара: '))
        except:
            print('Вы ввели не число!')
            return None
        return self

class Xerox(Equipment):
    def __init__(self, name, model, price, color):
        super().__init__(name, model, price)
        self.type = type
        self.format = format
        self.color = color

    def xer(self):
        print(f'Вы запустили {self.color} ксерокс {self.model} ')

    @staticmethod
    def user_input(self):
        self.name = 'Ксерокс'
        self.model = input(f'Введите модель ксерокса: ')
        self.color = input(f'Введите цвет печати: ')
        try:
            self.price = int(input(f'Введите цену товара: '))
        except:
            print('Вы ввели не число!')
            return None
        return self


scaner1 = Scaner('Сканер', 'Epson Perfection V19', 7140, 'Планшетный', 'A4', 10)
scaner2 = Scaner('Сканер', 'Xerox DocuMate 4760', 188338, 'Скоростной', 'A3', 60)
printer = Printer('Принтер', ' Brother HL-1202R', 7990, 'Лазерный', 'Черно-белый')
xerox1 = Xerox('Ксерокс', 'WorkCentre 6515N', 45990, 'Цветной')

xerox2 = Xerox.user_input(Xerox)
Scaner.scan()
xerox1.xer()
printer.run()

sklad = Sklad()
sklad.add_to_sklad(scaner1, 2)
sklad.add_to_sklad(scaner2, 5)
sklad.add_to_sklad(xerox1, 4)
sklad.add_to_sklad(printer, 6)
if xerox2 != None:
    sklad.add_to_sklad(xerox2, 4)
print('-' * 10 + 'Начальный склад' + '-' * 10)
print(sklad)
sklad = sklad.take_from_sklad(scaner1, 1)
sklad = sklad.take_from_sklad(printer, 6)
print('-' * 10 + 'Окончательный склад' + '-' * 10)
print(sklad)
print(f'Общее количество техники на складе: {sklad.account}')