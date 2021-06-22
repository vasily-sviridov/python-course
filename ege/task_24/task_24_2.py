import re


with open("24-171.txt") as f:
    lines = f.readlines()
    buffer = []
    for line in lines:
        buffer.append(re.findall(r"(XYZ(XYZ)*)", line)[0][0])


    print(len(max(buffer)) + 6)
            