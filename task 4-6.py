class Store:

    def __init__(self, name, price, quantity, num, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = num
        self.full_store = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Кол-во': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} кол-во {self.quantity}'

    def reception(self):
        try:
            model = input(f'Введите модель у-ва: ')
            model_p = int(input(f'Введите цену за шт.: '))
            model_q = int(input(f'Введите кол-во: '))
            model = {'Модель устройства': model, 'Цена за ед': model_p, 'Количество': model_q}
            self.my_unit.update(model)
            self.my_store.append(self.my_unit)
            print(f'Итого -\n {self.my_store}')
        except:
            return f'Error'

        print(f'Для выхода введите - Exit, для продолжения нажмите Enter: ')
        n = input(f'---> ')
        if n == 'Exit' or n == 'exit':
            self.full_store.append(self.my_store)
            print(f'Склад:\n {self.full_store}')
            return f'Exit'
        else:
            return Store.reception(self)


class Phone(Store):
    def to_phone(self):
        return f'to phone smbd {self.numb} times'


class Laptop(Store):
    def to_type(self):
        return f'to work with files {self.numb} times'


class Copier(Store):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


one = Phone('Apple', 50000, 5, 10)
two = Laptop('DELL', 120000, 5, 10)
three = Copier('Canon', 1500, 1, 15)
print(two.reception())
print(three.reception())
print(one.to_phone())
print(three.to_copier())
