class add(Exception):

    def func_str(self, res):
        try:
            for el in res:
                if type(el) == str:
                    raise add("В списке присутствует элемент типа данных <<str>>: ")

        except add as err:
            print(err, el)

    def func_list(self, res):
        try:
            for el in res:
                if type(el) == list:
                    raise add("В списке присутствует элемент типа <list>: ")
        except add as err:
            print(err, el)


input_list = [2, 1.2, 'str-элемент', bool(10), ['ana', 1, 'aka']]
print("Введенный список: ", input_list, "\n")
err = add()
err.func_list(input_list)
err.func_str(input_list)
