def add(x, y):
    x = float(x)
    y = int(y)
    result = 1
    if x <= 0 or y >= 0:
        return "Введите данные корректно."
    for _ in range(abs(y)):
        result /= x
    return result

print(add(float(input("Введите значение x: ")), int(input("Введите значение y: "))))
