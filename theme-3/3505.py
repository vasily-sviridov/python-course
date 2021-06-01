a = int(input())
b = int(input())
c = int(input())

max_number = a
if b > max_number:
    max_number = b
if c > max_number:
    max_number = c

print(max_number)