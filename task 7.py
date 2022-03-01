import json

with open(r"C:\Users\DELL\PycharmProjects\python\task 7.txt", 'r', encoding="utf-8") as file:
    dict = [{}, {}]
    total = 0
    count = 0
    for i in file:
        res = i.strip().split()
        profit = int(res[2]) - int(res[3])
        dict[0][res[0] + res[1]] = profit

        if profit > 0:
            total += profit
            count += 1

    dict[1]['average'] = total / count
print(dict)

with open(r"C:\Users\DELL\PycharmProjects\python\package.json", 'w', encoding="utf-8") as json_file:
    json.dump(dict, json_file, indent = 4)