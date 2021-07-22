
class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        string = ''
        for el in self.my_list:
            for i in el:
                string += str(i) + ' '
            string += '\n'
        return string

    def __add__(self, other):
        if len(self.my_list) != len(other.my_list) or len(self.my_list[0]) != len(other.my_list[0]):
            print('Размеры матриц должны совпадать!')
            return None
        else:
            matr = []

            for i, el in enumerate(self.my_list):
                matr.append([self.my_list[i][j] + other.my_list[i][j] for j, elem in enumerate(el)])

            return Matrix(matr)

my_list1 = [[1,2,3], [4,5,6]]
my_list2 = [[11,12,13], [14,15,16]]

matr1 = Matrix(my_list1)
matr2 = Matrix(my_list2)
print(f'Первая матрица: \n{matr1}')
print(f'Вторая матрица: \n{matr2}')
print(f'Сумма матриц: \n{matr1+matr2}')