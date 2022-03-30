# Подсчитать сумму цифр в вещественном числе.

a = float(input('Введите число: '))
# h = str(a)
# count = 0
# for i in range(len(h)):
#     if h[i] != '.':
#         count += int(h[i])
# print(count)

g = []
s = str(a)
for i in s:
    if i != '.':
        g.append(int(i))
print(sum(g))