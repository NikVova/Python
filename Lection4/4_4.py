# Написать программу преобразования
# десятичного числа в двоичное

a = int(input('Введите десятичное число: '))
# list_1 =[]
# while a > 0:
#     list_1.append(a % 2)
#     a = a // 2
# print(*list_1[::-1], sep ='')

a_string =''
while a > 0:
    a_string = str(a % 2) + a_string
    a //= 2
print(int(a_string))