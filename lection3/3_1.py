# Дан словарь,найти сумму всех ключей и значений словаря.

g = {1: 3, 5: 5, 6: 4, 7: 6}
summa1 = 0
summa2 = 0
# for i in g:
#     summa1 += i
#     summa2 += g[i]
# print(summa1, summa2)
print(*g.values())
print(*g.keys())
for k in g.values():
    summa1 += k
print(summa1)