# Определить, позицию второго вхождения строки в списке либо сообщить,
# что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#  список: [], ищем: "123", ответ: -1

a = ['a', 123, 'fsf', 'a']
b = 'a'
count = 0
if a.count(b) < 2:
    print(-1)
else:
    for i in range(len(a)):
        if a[i] == b:
            count += 1
            if count > 1:
                print(i)
                break

