from functools import cache

@cache
def f(n):
    if n <= 3:
        return n + 3
    elif n > 3 and f(n - 1) % 2 == 0:
        return f(n - 2) + n
    elif n > 3 and f(n - 1) % 2 != 0:
        return f(n - 2) + 2 * n

sum = 0
for i in range(40, 51):
    sum += f(i)

print(sum)