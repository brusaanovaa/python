dict = {}
with open(r"C:\Users\DELL\PycharmProjects\python\task6.txt", encoding="utf-8") as file:
    for line in file:
        name, stats = line.split(":")
        name_sum = sum(map(int, "".join([i for i in stats if i == " " or "9" >= i >= "0"]).split()))
        dict[name] = name_sum
print(f"{dict}")
