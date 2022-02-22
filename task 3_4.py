def add():
        x = 0
        list = input("Введите числа или stop: ")
        for i in list:
            if i == 'stop':
                return x, True
            try:
                x += int(i)
            except ValueError:
                pass
        return x, False