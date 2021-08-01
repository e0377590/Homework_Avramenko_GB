
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)
    def get_total_income(self):
        print(self._income['wage']+self._income['bonus'])

worker_1 = Worker('Anna', 'Avramenko', 'Engineer', 60000, 20000)
position_1 = Position('Anna', 'Avramenko', 'Engineer', 60000, 20000)
worker_2 = Worker('Yury', 'Avramenko', 'Teacher', 45000, 10000)
position_2 = Position('Yury', 'Avramenko', 'Teacher', 45000, 10000)
worker_3 = Worker('Vasilii', 'Kosmachev', 'Programmer', 60000, 120000)
position_3 = Position('Vasilii', 'Kosmachev', 'Programmer', 60000, 120000)

my_list = [position_1, position_2, position_3]
for el in my_list:
    el.get_full_name()
    el.get_total_income()