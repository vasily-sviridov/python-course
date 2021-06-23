"""

"""

expr = 5 * 6561 ** 46 + 5 * 729 ** 15 - 5 * 5832 - 5
result = ""
while expr:
    result += str(expr % 9)
    expr //= 9

print(result.count("4"))