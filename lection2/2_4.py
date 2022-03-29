# Дано пятизначное или шестизначное натуральное число.
# Напишите программу, которая изменит порядок его последних пяти цифр на обратный.
def func_porydok(chislo):
    if len(chislo) == 6:
        c = chislo[1:]
        d = chislo[0]
        print(int(chislo + c[::-1]))
    else:
        print(int(chislo[::-1]))
