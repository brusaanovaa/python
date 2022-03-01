class Worker:
    name = "Иван"
    surname = "Пушкин"
    position = "Бухгалтер"
    profit = 25000
    bonus = 5000
    rev = {"Оклад": profit,
           "Премия": bonus}
    result = 0


class Position(Worker):
    def get_full_name(self):
        return f"{self.position}\n{self.name} {self.surname}"

    def get_full_profit(self):
        self.result = self.profit + self.bonus
        return f"\nДоход с учётом премии = {self.result}"


w = Worker()
print(w.name)
print(w.surname)
print(w.position)
print(w.profit)

p = Position()
print("\n---\nОбщая информация по сотруднику:")
print(p.get_full_name() + str(p.get_full_profit()) + " " + str(w.rev))
