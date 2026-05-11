students = {
    "민수": 85,
    "지은": 92,
    "서준": 78,
    "하린": 95,
    "도윤": 88,
    "예은": 73,
    "시우": 81,
    "유진": 99,
    "현우": 67,
    "채원": 90
}

print(students)

def get_a_student(students):
    a_student = []
    for name, score in students.items():
        if score >= 90:
            a_student.append(name)
    return a_student

print("A등급 학생: ", get_a_student(students))