"""
Маша составляет шестибуквенные слова перестановкой букв слова КАПКАН. При этом она избегает слов с двумя подряд одинаковыми буквами. Сколько различных кодов может составить Маша?
"""

import itertools

s = set()

for (a, b, c, d, e, f) in itertools.permutations('капкан'):
      if a != b and b != c and c != d and d != e and e != f:
          s.add(a + b + c + d +e +f)

print(len(s))
