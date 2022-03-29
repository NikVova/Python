# Найти расстояние между двумя точками пространства
import math

print('Введите коордитнаты точки a по оси X и Y: ')
ax = float(input('X:'))
ay = float(input('Y:'))
print('Введите коордитнаты точки b по оси X и Y: ')
bx = float(input('X:'))
by = float(input('Y:'))

ab = math.sqrt(((bx - ax)**2) + ((by - ay)**2))
print(round(ab, 3))

