# Определить, присутствует ли в заданном списке строк,
# некоторое число

spisok = ['412', 'ads21', '421412dasads']
b = int(input('Введите число: '))
# b_str = str(b)
# for i in spisok:
#     if b_str in i:
#         print(True)
#         break
#
def func_1(array, g):
    g_str = str(g)
    for i in array:
        if g_str in i:
            return True

print(func_1(spisok,b))