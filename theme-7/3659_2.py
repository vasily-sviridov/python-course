number = int(input())

a, b = 0, 1
while a <= number + 1:
    a, b = b, a + b

print(a)