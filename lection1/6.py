#Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
a = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
Day = int(input('Введите номер дня недели: ')) -1
if 0 <= Day <= 6:
    print(a[Day])
    if Day > 4:
        print('Выходной')
    else:
        print('Будний день')
else:
    print('Нет такого дня')

