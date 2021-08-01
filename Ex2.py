
class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length
    def mass(self):
        return self._width * self._length * 25 * 5

new_road = Road(5000, 20)
print(new_road.mass())