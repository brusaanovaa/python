rev = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержек: "))

if rev > costs:
    prof = rev - costs
    loss = prof / rev
    print(f"Фирма отработала с прибылью")

    staff = int(input("Введите численность имеющегося персонала: "))
    print(f"{prof/staff} с расчётом на одного сотрудника")
else:
    print("Фирма отработала в убыток")