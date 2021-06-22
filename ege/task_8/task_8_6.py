"""
Миша составляет 6-буквенные коды из букв С,А,Л,Ь,С,А. Каждая допустимая гласная буква может входить в код не более одного раза. Сколько кодов может составить Миша?
"""

from itertools import product

s = set()
for (a, b, c, d, e, f) in product("САЛЬСА", repeat=6):
    word = a + b + c + e + d + f
    if word.count("А") <= 1:
        s.add(word)

print(len(s))