a = 1
while True:
    found = False
    for x in range(56 * 48):
        if not ({2, 4, 8, 12, 15} <= (not ({3, 6, 8, 15}) or (a))):
            found = True
            break
    
    if not found:
        print(a)
        break

    a += 1
