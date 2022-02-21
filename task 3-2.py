def add(name, surname, b_year, city, email, phone_number):
    return f'Имя: {name}, Фамилия: {surname}, Год рождения: {b_year}, ' \
           f'Город: {city}, Почта: {email}, Номер телефона: {phone_number}'


print(add(name=input('Введите имя: '),
          surname=input('Введите фамилию: '),
          b_year=input('Введите год рождения: '),
          city=input('Введите город: '),
          email=input('Введите почту: '),
          phone_number=input('Введите номер телефона: ')))
