"""
(Е. Джобс) Определите, при каком наибольшем введённом значении переменной S программа выведет число 257?

s = int(input())
s //= 8
n = 2
while s <= 102:
    s += 4
    n = n * 2 - 1

print(n)

"""


def f(x):
    s = x
    s //= 8
    n = 2
    while s <= 102:
        s += 4
        n = n * 2 - 1
    
    return n

for i in range(10000):
    if f(i) == 257:
        print(i)