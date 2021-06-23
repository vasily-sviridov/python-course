def div(n, m):
    return n % m == 0

a = 1
while a < 50:
    Flag = False
    for x in range(1, 1000):
        if not ((not div(x, a)) <= (div(x, 10) <= (not div(x, 12)))):
            Flag = True
            break

    if not Flag:
        print(a)

    a += 1
