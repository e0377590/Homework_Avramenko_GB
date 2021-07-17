import time

class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        if self.__color == 'red':
            print('red')
            time.sleep(7)
        elif self.__color == 'yellow':
            print('yellow')
            time.sleep(2)
        elif self.__color == 'green':
            print('green')
            time.sleep(5)
        else: print('Error: the color must be red, yellow or green!')

my_list = ['red', 'yellow', 'green', 'blue']

for el in my_list:
    traffic_light = TrafficLight(el)
    traffic_light.running()
