"""
(Е. Джобс) Настя составляет 6-буквенные слова, в которых есть только буквы Д, Ж, О, Б, С, причём буквы Д, О, С встречаются ровно по одному разу. Буква Ж встречается не более 2 ращз, а буква Б может встречаться любое количество раз или не встречаться вовсе. Словом считается любая допустимая последовательность букв, не обязательно осмысленная. Сколько различных слов может составить Настя.
"""

from itertools import product

s = set()
for (a, b, c, d, e, f) in product("ДЖОБС", repeat=6):
    word = a + b + c + e + f
    if word.count("Д") <= 1 and word.count("О") <= 1 and word.count("С") <= 1 and word.count("Ж") <= 2:
        s.add(word)

print(len(s))