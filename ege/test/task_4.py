"""

"""


string = "1" * 170 + "3" * 100 + "2" * 7
while "11" in string:
    string = string.replace("112", "4", 1)
    string = string.replace("113", "2", 1)
    string = string.replace("42", "3", 1)
    string = string.replace("43", "1", 1)

print(string)