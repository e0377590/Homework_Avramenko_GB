
class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationary):
    def draw(self):
        print('Вы рисуете ручкой')

class Pencil(Stationary):
    def draw(self):
        print('Вы рисуете карандашем')

class Handle(Stationary):
    def draw(self):
        print('Вы рисуете маркером')

st = Stationary('Канцелярия')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

st.draw()
pen.draw()
pencil.draw()
handle.draw()