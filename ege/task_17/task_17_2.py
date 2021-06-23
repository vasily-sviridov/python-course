"""
Назовём натуральное число подходящим, если ровно два из его делителей входят в список (7, 13, 17, 19). Найдите все подходящие числа, принадлежащие отрезку [25000; 35000]. В ответе запишите два целых числа: сначала количество, затем сумму цифр всех найденных чисел.
"""

from itertools import accumulate

def dividors_generator(n):
    buffer = set()
    for i in range(2, 20):
        if n % i == 0:
            buffer.add(i)

    return buffer

buffer = set()
for i in range(25000, 35000):
    count = 0
    dividors = dividors_generator(i)
    for j in dividors:
        if (j in [7, 13, 17, 19]):
            count += 1

    if count == 2:
        buffer.add(i)

print(len(buffer))

sum = 0
for i in buffer:
    numbers = [int(j) for j in str(i)]
    print(numbers)

print(sum)
    