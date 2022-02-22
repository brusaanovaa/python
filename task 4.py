dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four':  'Четыре'}
with open(r'C:\Users\DELL\Downloads\text1.txt', 'r') as eng_file:
    with open(r'C:\Users\DELL\Downloads\text2.txt', 'w') as rus_file:
        for i in eng_file:
            en, *num = i.split()
            ru = dict[en]
            rus_file.write(' '.join([ru] + num) + '\n')