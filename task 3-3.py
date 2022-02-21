def add(x, y, z):
    try:
        return sum((x, y, z)) - min(x, y, z)
    except TypeError:
        return "Попытайтесь ещё раз."


print(add(int(input("Введите значение x: ")), int(input("Введите значение y: ")), int(input("Введите значение z: "))))