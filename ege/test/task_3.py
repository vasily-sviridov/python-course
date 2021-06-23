"""
Все четырёхбуквенные слова, составленные из букв А, Л, Г, О, Р, И, Т, М записаны в алфавитном порядке и пронумерованы, начиная с 1. Начало списка выглядит так:
"""

from itertools import product

count = 0
last_pos = 0
for (a, b, c, d) in product(sorted("АЛГОРИТМ"), repeat=4):
    word = a + b + c + d
    count += 1
    if word.endswith("ИМ"):
        last_pos = count

print(last_pos)