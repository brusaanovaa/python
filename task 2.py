with open(r"C:\Users\DELL\PycharmProjects\python\rus.txt", "r", encoding='utf-8') as file_obj:
    lines = 0
    letters = 0

    for line in file_obj:
        lines += 1
        letters = len(line.split())

print(f"Кол-во слов/символов в строке = {letters}")
print(f"Кол-во строк = {lines}")
