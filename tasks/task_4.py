json = input()
json_splitted = json[1:len(json) - 1].split(",")

for i in range(json.count(",") + 1):
    key = json_splitted[i][1:json_splitted[i][1::].find('"', 1) + 1]
    value = json_splitted[i].split(":")[1]
    print({key: value})

