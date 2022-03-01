class add(Exception):

    def division_func(self, x, y):
        try:
            res = round(x / y, 2)
        except ZeroDivisionError:
            print(f"{x} / {y} = Ошибка вычислений.\n")
        else:
            print(f"{x} / {y} = {res} \n")


res = add()

res.division_func(3, 2)
res.division_func(1, 0)
res.division_func(-1, 3)
res.division_func(0, 4)