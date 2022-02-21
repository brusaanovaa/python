def add(x, y):
        x = float(x)
        y = int(y)
        if x <= 0 or y >= 0:
            return "Введите данные корректно."
        try:
            return x**y
        except ValueError:
            print("Попытайтесь ещё раз.")
            return

print(add(float(input("Введите значение x: ")), int(input("Введите значение y: "))))