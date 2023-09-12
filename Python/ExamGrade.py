student_grade = int(input('Input a number between 1 and 100: '))


if student_grade < 50:
    print("Fail")
elif student_grade == 50 or (student_grade > 50 and student_grade <= 60):
    print("Pass")
elif student_grade == 61 or (student_grade > 61 and student_grade <= 70):
    print("Merit")
elif student_grade == 71 or (student_grade > 71 and student_grade <= 100):
    print("Distinction")
else:
    print("'Error: marks must be between 1 and 100")