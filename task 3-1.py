def add(x, y):
    try:
        return float(x) / float(y)
    except ValueError:
        return "Попытайтесь ещё раз."
    except ZeroDivisionError:
        return "На ноль делить нельзя."


print(add(input("Введите значение x: "), input("Введите значение y: ")))
