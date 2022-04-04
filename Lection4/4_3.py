# Найти сумму чисел списка стоящих на нечетной
# позиции

a = [2, 4, 5, 6, 2, 10, 214]
count = 0
# for i in range(1, len(a), 2):
#     count += a[i]
# print(count)

for i in range(len(a)):
    if i % 2 != 0:
        count += a[i]
print(count)
