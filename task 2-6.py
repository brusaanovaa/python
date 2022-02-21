goods = []
while input("Хотите добавить продукт? Введите Да/Нет: ") == 'Да':
    number = input("Введите номер: ")
    f_key = input("Введите название: ")
    f_value = input("Введите стоимость: ")
    f_count = input("Введите кол-во: ")
    f_unit = input("Введите единицу измерения: ")
    features = {'Название': f_key,
                'Цена': f_value,
                'Кол-во': f_count,
                'Единица': f_unit}
    goods.append(tuple([number, features]))

print(goods)

analytics = {'Название': [], 'Цена': [], 'Кол-во': []}
for product in goods:
    analytics['Название'].append(product[1]['Название'])
    analytics['Цена'].append(product[1]['Цена'])
    if product[1]['Кол-во'] not in analytics['Кол-во']:
        analytics['Кол-во'].append(product[1]['Кол-во'])

print(analytics)
