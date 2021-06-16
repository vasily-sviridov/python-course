from itertools import permutations

buffer = set(permutations("АССАСИН", r=7))
print(len(buffer))