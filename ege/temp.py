a = 1
while True:
    for x in range(1000):
        for y in range(1000):
            if not ((2 * y + 4 * x < a) or (x + 2 * y > 80)):
                break
	   else:
		  continue
	   break
    else:
        print(a)
    a += 1
