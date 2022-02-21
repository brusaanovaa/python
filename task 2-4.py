text = input("Введите слова с пробелами: ")
words = text.split()
num = 1
for element in range(text.count(' ') + 1):
    if len(str(element)) <= 10:
        print(f" {num}. {words [element] [0:10]}")
        num += 1
