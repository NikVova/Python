# Пользователь задаёт две строки.
# Определить количество вхождений одной строки в другой.

stroka_1 = input('Введите первую строку: ')
stroka_2 = input('Введите вторую строку: ')
count = 0
i = 0
while i < len(stroka_1):
    for j in range(len(stroka_2)):
        if i < len(stroka_1):
            if stroka_1[i] == stroka_2[j]:
                if j == len(stroka_2) -1:
                    count += 1
                i = i +1
print(count)