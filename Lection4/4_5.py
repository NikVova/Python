# Найти Наименьшее Общее Кратное двух чисел
from math import gcd

a = int(input())
b = int(input())

# print(a * b // gcd(a,b)) # встроенная библиотека

# s = (a * b) /2
# # s = min(a, b)
# while True:
#     if s % a == 0 and s % b == 0:   # плохой способ
#         break
#     else:
#         s += 1
# temp = 0
# while True:
#     if s % a == 0 and s % b == 0:
#         break
#     else:
#         s /= 2
# print(int(s))