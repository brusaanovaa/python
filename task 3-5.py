def add():
    x = 0
    while True:
        list = input("Введите числа или stop: ").split()
        for i in list:
            try:
                x += float(i)
            except ValueError:
                print (x,'Возвращаетесь ещё!')
                break
        else:
            print(x)
            continue
        break
    return
add()