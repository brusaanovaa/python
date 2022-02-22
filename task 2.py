list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
n = [elem for elem in list if elem > list[list.index(elem)-1] and list.index(elem) != 0]

print(n)
