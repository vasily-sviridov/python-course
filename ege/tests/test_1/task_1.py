def div(n, m):
    return n % m == 0


a = 1
while True:
    flag = False
    for x in range(1, 34 * 51):
        if not ((div(x, 34) and (not div(x, 51))) <= ((not div(x, a)) or div(x, 51))):
            flag = True
            break

    if not flag:
        print(a)
        break

    a += 1
