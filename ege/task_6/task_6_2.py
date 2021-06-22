"""
Ниже записана программа, которая вводит натуральное число x, выполняет преобразования, а затем выводит результат. Укажите наименьшее значение x, при вводе которого программа выведет число 45.

x = int(input())
a = x - 61
b = 3 * x - 138

while a != b:
    if a > b:
        a -= b
    else:
        b -= a

    print(a)
"""

found = False
for x in range(62, 200):
    a = x - 61
    b = 3 * x - 138

    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

        if a == 45:
            print(x)
            found = True
            break

    if found:
        break

