students = [
    {"name": "Lara",  "age": 23, "track": "AI",   "hours_studied": 40, "scores": [85, 90, 78]},
    {"name": "Omar",  "age": 31, "track": "Data", "hours_studied": 12, "scores": [60, 55, 70]},
    {"name": "Rim",   "age": 27, "track": "AI",   "hours_studied": 55, "scores": [95, 88, 92]},
    {"name": "Karim", "age": 19, "track": "Web",  "hours_studied": 8,  "scores": [50, 65, 40]},
    {"name": "Nour",  "age": 25, "track": "AI",   "hours_studied": 30, "scores": [75, 80, 85]},
    {"name": "Sami",  "age": 35, "track": "Data", "hours_studied": 48, "scores": [88, 91, 79]},
]

# task 1
print(students[0]["name"])
print(students[-1]["name"])
# task 2
print(students[2]["scores"])

# task 3
for student in students:
    print(f"{student['name']} is {student['age']} years old and studies {student['track']}")

# task 4
ai_students = []
for student in students:
    if student["track"] == "AI":
        ai_students.append(student)

# print(ai_students)
print(len(ai_students))

# task 5
ai_students_lc = [student for student in students if student["track"] == "AI"]
print(len(ai_students_lc))
print(ai_students_lc == ai_students)

# task 6
listStudent = []
for student in students:
    if student["hours_studied"] > 30:
        listStudent.append(student["name"])

print(listStudent)

# task 7
listStudent2 = []
for student in students:
    if student["age"] > 24 and student["track"] == "AI":
        listStudent2.append(student)

print(listStudent2)

# task 8
total_age = 0
for student in students:
    total_age+=student["age"]

print(total_age/len(students))

# task 9
total_hours = 0
for student in students:
    total_hours+=student["hours_studied"]

print(total_hours)

# task 10
top_student = students[0]
for student in students:
    if student["hours_studied"] > top_student["hours_studied"]:
        top_student = student

print(f"{top_student['name']} studied the most: {top_student['hours_studied']} hours")

# task 11
for student in students:
    avg = round(sum(student["scores"]) / len(student["scores"]), 1)
    print(f"{student['name']}: {avg}")

# task 12
new_list = [{"name": student["name"], "average_score": round(sum(student["scores"]) / len(student["scores"]), 1)} for student in students]
print(new_list)

# task 13
track_counts = {}
for student in students:
    track = student["track"]
    if track in track_counts:
        track_counts[track] += 1
    else:
        track_counts[track] = 1

print(track_counts)

# task 14
# A set automatically removes duplicate values to keep only unique tracks, unlike a list which preserves duplicates
set_track = set()
for student in students:
    set_track.add(student["track"])

print(set_track)

# task 15
def calculate_average(scores):
    return round(sum(scores) / len(scores), 1)

# task 16
def get_top_students(students_list, min_avg=85):
    top_names = []

    for student in students_list:
        if calculate_average(student["scores"]) >= min_avg:
            top_names.append(student["name"])

    return top_names

print(get_top_students(students, 90))

# task 17
def filter_by_track(students_list, track_name):
    student_track = []

    for student in students_list:
        if student["track"] == track_name:
            student_track.append(student["name"])

    return student_track

print(filter_by_track(students, "AI"))

# task 18
def summarize_student(student):
    avg = calculate_average(student["scores"])
    return f"{student['name']} ({student['track']}) - Avg: {avg}, Hours: {student['hours_studied']}"

print(summarize_student(students[0]))

# task 19
def mini_pipeline(students_list, target_track="AI", min_avg=85):
    track_students = filter_by_track(students_list, target_track)
    summaries = []

    for student in students_list:
        if student["name"] in track_students:
            summaries.append(summarize_student(student))

    top_students = get_top_students(students_list, min_avg)

    return summaries, top_students


track_summaries, top_list = mini_pipeline(students, "AI", 85)

for s in track_summaries:
    print(s)

print("Top students:", top_list)
