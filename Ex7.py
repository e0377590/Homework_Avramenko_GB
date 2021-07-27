class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        if self.y > 0:
            return str(self.x)+'+i*'+str(self.y)
        elif self.y == 0:
            return str(self.x)
        else:
            return str(self.x)+'-i*'+str(abs(self.y))

    def __add__(self, other):
        return Complex(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Complex(self.x*other.x-self.y*other.y, self.x*other.y+self.y*other.x)

x1 = Complex(2,3)
x2 = Complex(-1,1)
print(f'Умножение двух комплексных чисел {x1*x2}')
print(f'Сложение двух комплексных чисел {x1+x2}')
print(f'Вычитание двух комплексных чисел {x1-x2}')
