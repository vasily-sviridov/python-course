str = "8" * 1000

while "999" in str or "888" in str:
    if "888" in str:
        str.replace("888", "9")
    else:
        str.replace("999", "8")

print(str)

# 10 14
