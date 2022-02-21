num = int(input("Введите новый элемент рейтинга: "))
list = [9, 8, 7, 6, 5]
c = list.count(num)
for elem in list:
    if c > 0:
        i = list.index(num)
        list.insert(i+c, num)
    else:
        if num > elem:
            j = list.index(elem)
            list.insert(j, num)
            break
        elif num < list[len(list) - 1]:
            list.append(num)
print(list)
print(list.index(num))