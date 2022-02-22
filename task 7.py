from math import factorial

n = int(input("Введите цифру: "))


def add(x):
    for i in range(x):
        print(n, end='! = ')
        yield factorial(n)
        break


for elem in add(n):
    print(elem)
