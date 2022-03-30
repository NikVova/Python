# Найти сумму отрицательных элементов в списке

list_1 = [1, -2, 10, -4242, - 2442]
count_negativ = 0
for i in list_1:
    if i < 0:
        count_negativ += i
print(count_negativ)