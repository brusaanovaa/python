def add(word):
    #return word.word[0].upper() + word[1:].lower()
    #print(add(input('Введите слово маленькими буквами: ')))
    next = word.rsplit()
    end = []
    for i in next:
        elem = str(i)
        f_letter = elem[:1].upper()
        word = f_letter + elem[1:]
        end.append(word)
    return end
print(add(input('Введите строку маленькими буквами с пробелами: ')))
