from itertools import count

for elem in count(3):
    if elem > 10:
        break
    print(elem)