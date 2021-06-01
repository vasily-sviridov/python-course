import math


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

x1 = float(input())
y1 = float(input())

x2 = float(input())
y2 = float(input())

print(distance(x1, y1, x2, y2))