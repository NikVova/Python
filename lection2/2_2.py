# Написать функцию-калькулятор с операциями: Умножение,деление, остаток от деления,
# вычитание, целочисленное деление.

def calc(a, b, sign):
    if sign == '+':
        return a + b
    elif sign == '/' and b !=0:
        return a / b
    elif sign == '*':
        return a * b
    elif sign == '%':
        return a % b
    elif sign == '//':
        return a // b
    elif sign == '-':
        return a - b

a = int(input())
b = int(input())
sign = input('Введите знак: ')
if b == 0 and ( sign == "/" or sign == "%" or sign == "//"):
    print('На ноль делить нельзя ')
else:
    print(calc(a, b, sign))