def f(x):
    a = 0
    b = 1
    while x > 0:
        if x % 2 == 0:
            a = a + x % 9
        else:
            b = b * (x % 9)
        x //= 9

    return a, b

for i in range(1000):
    if f(i) == (1, 9):
        print(i) 