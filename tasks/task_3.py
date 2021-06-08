import operator

count_students = int(input())
student_marks = {}
student_marks_count = {}

for i in range(count_students):
    mapped_list = input().split(": ")

    if not mapped_list[0] in student_marks:
        student_marks[mapped_list[0]] = int(mapped_list[1])
        student_marks_count[mapped_list[0]] = 1
    else:
        student_marks[mapped_list[0]] += int(mapped_list[1])
        student_marks_count[mapped_list[0]] += 1

result_db = {}
for i in student_marks:
    result_db[i] = round(student_marks[i] / student_marks_count[i])

print(f"Худший - {min(result_db, key=result_db.get)}")
print(f"Лучший - {max(result_db, key=result_db.get)}")