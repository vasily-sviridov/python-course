def conv(n):
    result = ""
    while n:
        result += str(n % 8)
        n //= 8
    
    return result[::-1]

buffer = []
for i in range(99, 999):
    if i % 10 == 9 and conv(i)[-1] == "1" and i % 18 != 0:
        buffer.append(i)

print(len(buffer), max(buffer))