a = 1
while True:
    found = False
    for x in range(56 * 48):
        if not ((x & 56 != 0) <= ((x & 48 == 0) <= (x & a != 0))):
            found = True
            break
    
    if not found:
        print(a)
        break

    a += 1
