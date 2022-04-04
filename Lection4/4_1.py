# 1)Даны два словаря: dictionary_1 = {'a': 300, 'b': 400} и
# dictionary_2 = {'c': 500, 'd': 600}. Объедините их в
# один при помощи встроенных методов языка Python.

dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}

dictionary_3 = dictionary_1.copy()       # Копирование словаря
dictionary_3.update(dictionary_2)      # Добавление словаря 2 в 3
print(dictionary_3)