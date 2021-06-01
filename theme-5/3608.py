import math


value = float(input())
if value > 1:
    a = math.floor(value)
    b = value - a
    print(round(b, 2))
else:
    print(value)


"""
Это решение не будет работать из-за устройства компьютерной арифметики
value = float(input())
print(value - int(value))
"""