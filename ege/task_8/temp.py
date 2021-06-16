with open("file_name.txt") as file:
    data = file.read() # получить всю информацию в строке
    data_by_lines = file.readlines() # получить всю информацию построчно в спискок