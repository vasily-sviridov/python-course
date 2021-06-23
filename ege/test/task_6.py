"""
(Е. Джобс) Обозначим через div(n, m) утверждение «натуральное число n делится без остатка на натуральное число m». Для какого наименьшего натурального числа A формула
        (div(x, A – 21) && div(x, 40 – A)) -> div(x, 90)
тождественно истинна, то есть принимает значение 1 при любом натуральном х?
"""

def div(n, m):
    return n % m == 0

a = 1
while True:
    found = False
    for x in range(1, 1000):
        if a == 21 or a == 40:
            continue

        if not ((div(x, a - 21) and div(x, 40 - a)) <= div(x, 90)):
            found = True
            break
    
    if not found and a != 21 and a != 40:
        print(a)
        break

    a += 1