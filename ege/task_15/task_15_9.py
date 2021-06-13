buffer = []

a = 1
while True:
    found = False
    for x in range(1000):
        if not ((x & 25 != 1) or ((x & 34 == 2) <= (x & a == 0))):
            found = True
            break

    if not found:
        print(a)
        break

    a += 1