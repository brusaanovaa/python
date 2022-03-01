f = open(r'C:\Users\DELL\Downloads\Русанова.txt', 'w')
print("Введите текст в файл: ")
while True:
    text = input()
    f.write(text + '\n')
    if text == "":
        break
f.close()
