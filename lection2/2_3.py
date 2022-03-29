# Дана строка текста. Напишите программу для подсчета стоимости строки,
# исходя из того, что один любой символ (в том числе пробел) стоит 60 копеек.
# Ответ дайте в рублях и копейках.


def function(stroka):
    cop = len(stroka) * 60
    rub = cop // 100
    cop -= rub * 100
    return str(rub) + str(cop)

storka = input('Введите строку: ')
print(function(storka))
