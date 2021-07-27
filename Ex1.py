
class Data:
    def __init__(self, name):
        self.name = name

    @classmethod
    def first_method(cls, string):
        return list(map(int, string.split('-')))

    @staticmethod
    def second_method(string):
        my_list = Data.first_method(string)
        return my_list[0] < 32 and my_list[0] > 0 and my_list[0] > 1 and my_list[1] < 13 and my_list[2] > 1910 and my_list[2] < 2022

string = '05-02-1988'
print(Data.first_method(string))
print(f'Данные верны? {Data.second_method(string)}')
string = '05-13-1988'
print(Data.first_method(string))
print(f'Данные верны? {Data.second_method(string)}')
