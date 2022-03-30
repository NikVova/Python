# Найти максимальный и минимальный элемент в списке чисел.

list_new = [1, 2, 10, 4242, 2442]

value_max = list_new[0]
value_min = list_new[0]
for i in list_new:
    if value_max < i:
        value_max = i
    if value_min > i:
        value_min = i
print(value_max, value_min)