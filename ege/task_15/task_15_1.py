a = 1
while True:
    found = False
    for x in range(1, 70 * 18 * 42):
        if not ((x & 56 != 0) <= ((x & 48 == 0) <= (x & a != 0))):
            found = True
            break

    if not found:
        print(a)

    a += 1
