# Дан словарь,найти сумму всех ключей и значений словаря.

g = {1: 3, 5: 5, 6: 4, 7: 6}
summa1 = 0
summa2 = 0
# for i in g:
#     summa1 += i
#     summa2 += g[i]
# print(summa1, summa2)

# for i in g.values():
#     summa1 += i
# for k in g.keys():
#     summa2 += k
# print(summa1, summa2)

for i, g in g.items():
    summa1 += i
    summa2 += g
print(summa1, summa2)