class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def police(self):
        if self.is_police:
            return 'Полицейская машина -'
        else:
            return 'Гражданская машина -'

    def info(self):
        return f" {self.color} {self.name}\nМаксимальная скорость: {self.speed} км/ч "

    def go(self):
        return "\nМашина поехала\n""---\n"

    def stop(self):
        return "\nМашина остановилась\n""---\n"

    def turn(self):
        return "\nМашина повернула\n""---\n"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car1 = TownCar(160, "Белый", "Ford", False)
print(car1.police() + car1.info() + car1.turn())

car2 = SportCar(250, "Синяя", "Audi", False)
print(car2.police() + car2.info() + car2.go())

car3 = WorkCar(0, "Чёрная", "Газель", False)
print(car3.police() + car3.info() + car3.stop())

car4 = PoliceCar(400, "Белая", "Kia", True)
print(car4.police() + car4.info() + car4.go())