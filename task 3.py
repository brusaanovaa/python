names = []
num = 0
res = 0
min_sal = 100000

with open(r"C:\Users\DELL\Downloads\rus.txt", "r", encoding='utf-8') as file_obj:
    for line in file_obj:
        num += 1
        name, inc = (elem for elem in line.split())
        inc = float(inc)
        if inc < min_sal:
            names.append(name)
        res += inc
    res /= num
print(f"Фамилии сотрудников, получающих < {min_sal} =", *names)
print("Средняя зарплата по сотрудникам =", res)
