from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def add(self):
        print("Тип одежды:", end=' ')

    @abstractmethod
    def add_(self):
        print("Параметр:", end=' ')

    @abstractmethod
    def _add(self):
        print("Расход ткани =", end=' ')


class Coat (Clothes):
    def add(self):
        super().add()
        print("Пальто")

    def add_(self):
        super().add_()
        print("Размер")

    def _add(self):
        super()._add()
        return float(self.value) / 6.5 + 0.5


class Suit (Clothes):
    def add(self):
        super().add()
        print("Костюм")

    def add_(self):
        super().add_()
        print("Рост")

    def _add(self):
        super()._add()
        return 2 * float(self.value) + 0.3


class Total:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return (self.a / 6.5 + 0.5) + (2 * self.b + 0.3)


coat_size = int(input("Введите размер пальто: "))
suit_size = int(input("Введите размер костюма: "))

print("\n")
c = Coat(coat_size)
c.add()
c.add_()
print("%.2f" % c._add())


print("\n")
s = Suit(suit_size)
s.add()
s.add_()
print("%.2f" % s._add())


t = Total(coat_size, suit_size)
print("\nИтого ткани: %.2f" % t.sum())