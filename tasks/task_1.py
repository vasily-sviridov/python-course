def count_duplicates():
    count_elements = int(input())

    search_db = []

    for i in range(count_elements):
        mapped_list = input().split(", ")
        search_db.append(mapped_list[0].lower())

    answer_db = {}

    for key in search_db:
        if search_db.count(key) > 1:
            answer_db[key] = search_db.count(key)

    for key in answer_db:
        print(f"{ {key} } = {answer_db[key]}")

count_duplicates()



