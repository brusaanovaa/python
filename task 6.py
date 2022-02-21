a = int(input("Введите результат за первый день в км: "))
b = int(input("Введите общий результат в км: "))
day_num = 1

while a < b:
    a = a + a/10
    day_num += 1
print(day_num)

