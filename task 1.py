f = open('file_task_01.txt', 'w')
print("Введите текст в файл: ")
while True:
    text = input()
    f.write(text + '\n')
    if text == "":
        break
f.close()
