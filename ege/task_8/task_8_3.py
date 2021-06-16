"""
№123
(А.Н. Носкин) Петя составляет семибуквенные слова перестановкой букв слова АССАСИН. Сколько всего различных слов может составить Петя?
"""

from itertools import permutations

buffer = set(permutations("АССАСИН", r=7))
print(len(buffer))