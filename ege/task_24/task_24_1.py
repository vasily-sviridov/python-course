"""
№173.
(Е. Джобс) Текстовый файл 24-173.txt состоит не более чем из 106 букв из набора A, B, C, D, E, F. Найдите максимальную длину подстроки, в которой ни одна тройка символов не записана два раза подряд. Например, в искомой подстроке не может быть фрагмента ABCABC.
"""


with open("24-173.txt") as f:
    data = f.read()
    length = 5
    length_max = 5
    for i in range(len(data) - 5):
        if data[i:i + 3] != data[i + 3:i + 6]:
            length += 1
            length_max = max(length_max, length)
        else:
            length = 5

    print(length_max)
