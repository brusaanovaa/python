int = 10
float = 10.1
str = "Rusanova"
list = [2, 3, 4, 5]
smth = ('Rusanova', 2001, [7, 4, 35], True)
smth2 = {"Япония": "страна"}

end_list = [int, float, str, list, smth, smth2]

for i in end_list:
    print(f'{i} is {type(i)}')