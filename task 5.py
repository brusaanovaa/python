from functools import reduce

list = [elem for elem in range(100, 1001) if elem % 2 == 0]


def add(elem1, elem):
    return elem1 * elem


print(reduce(add, list))
