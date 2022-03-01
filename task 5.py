from random import randint

with open(r"C:\Users\DELL\PycharmProjects\python\task5.txt", "w+", encoding="utf-8") as file:
    file.write(" ".join([str(randint(1, 100)) for _ in range(10)]))
    file.seek(0)
    print(sum(map(int, file.readline().split())))