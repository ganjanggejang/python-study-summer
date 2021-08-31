import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eliz', 'Freddie']

students_scores = {student: random.randint(1, 100) for student in names}

passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
# items()는 딕셔너리의 키와 값의 튜플을 가져오는 메서드


print(students_scores)
print(passed_students)











