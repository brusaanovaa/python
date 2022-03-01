class Stationery:
    def __init__(self, title="Рисунок"):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки: {self.title})")


class Pen(Stationery):
    def draw(self):
        print(f"\nЗапуск отрисовки ручкой: {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"\nЗапуск отрисовки карандашом: {self.title}")


class Marker(Stationery):
    def draw(self):
        print(f"\nЗапуск отрисовки маркером: {self.title}")


s = Stationery()
s.draw()

p_1 = Pen("Word")
p_1.draw()

p_2 = Pencil("Word2")
p_2.draw()

m = Marker("Word3")
m.draw()
