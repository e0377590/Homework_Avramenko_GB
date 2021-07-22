
class Cell:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number < other.number:
            print('Операция невозможна!')
            return None
        return Cell(self.number - other.number)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, value):
        for i in range(self.number // value):
            print('*' * value)
        print('*' * (self.number % value))

cell1 = Cell(15)
cell2 = Cell(12)
print(f'Сложение: {cell1 + cell2}')
print(f'Вычитание: {cell1 - cell2}')
print(f'Умножение: {cell1 * cell2}')
print(f'Деление: {cell1 / cell2}')

print('Первый вариант:')
cell1.make_order(5)
print('Второй вариант:')
cell2.make_order(5)
