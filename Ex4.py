class Car:
    def __init__(self, name, speed, color, is_police='None', direction = 'right'):
        self.name = name
        self.speed = speed
        self.is_police = is_police
        self.color = color
        self.direction = direction
    def go(self):
        print(f'A car {self.name} is moving')
    def stop(self):
        print(f'A car {self.name} is stopped')
    def turn(self):
        print(f'A car {self.name} turn {self.direction}')
    def show_speed(self):
        print(f'The current speed is {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('A maximal speed value is 60!!!')
        else:
            print(f'The current speed is {self.speed}')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('A maximal speed value is 40!!!')
        else:
            print(f'The current speed is {self.speed}')

class PoliceCar(Car):
    pass

Arkana = Car('Reno Arkana', 90, 'red')
Arkana.go()
Arkana.turn()
Arkana.show_speed()
print('-' * 100)

Creta = TownCar('Hyundai Creta', 60, 'grey', direction = 'left')
print(f'if {Creta.name} is police car? {Creta.is_police}')
Creta.show_speed()
print('-' * 100)

Panamera = SportCar('Porsche Panamera', 200, 'blue')
Panamera.stop()
Panamera.turn()
print(f'The color of {Panamera.name} is {Panamera.color}')
print('-' * 100)

Vesta = PoliceCar('Lada Vesta', 50, 'white', is_police=True, direction = 'left')
Vesta.turn()
Vesta.show_speed()
print('-' * 100)

Granta = WorkCar('Lada granta', 60, 'yellow')
print(f'Name of WorkCar is {Granta.name}')
Granta.turn()
Granta.show_speed()
