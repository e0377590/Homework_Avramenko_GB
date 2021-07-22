
class Clothes:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Coat(Clothes):
    @property
    def tissue_consumption(self):
        return self.value / 6.5 + 0.5

class Suit(Clothes):
    @property
    def tissue_consumption(self):
        return self.value * 2 + 0.3

caot = Coat('пальто', 5)
suit = Suit('костюм', 10)

print(f'Расход ткани на пальто: {round(caot.tissue_consumption, 2)}')
print(f'Расход ткани на костюм: {round(suit.tissue_consumption, 2)}')
print(f'Общий расход ткани на пальто и костюм: {round(caot.tissue_consumption+suit.tissue_consumption, 2)}')