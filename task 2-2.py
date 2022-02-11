list = input("Введите элементы списка: ").split()
indx = 0
if len(list) % 2 == 0:
    while indx < len(list):
        x = list[indx]
        list[indx] = list[indx + 1]
        list[indx + 1] = x
        indx += 2
else:
    while indx < len(list) - 1:
        x = list[indx]
        list[indx] = list[indx + 1]
        list[indx + 1] = x
        indx += 2
print(list)