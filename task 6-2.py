from itertools import count, cycle

x = 10
list = [elem for elem in range(5)]
result_1 = count()
result_2 = cycle(list)

print([next(result_1) for elem in range(x)])
print([next(result_2) for elem in range(x)])
