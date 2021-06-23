"""

"""


with open("24-5.txt") as f:
    data = f.readline()

    count = 0
    for i in range(len(data) - 1):
        if data[i] == "(" and data[i + 1] == ")":
            count += 1
            i += 2
        if count == 10000:
            print(i - 1)
            break
