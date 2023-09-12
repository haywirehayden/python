student_level = int(input('Input level 1 or level 2: '))
student_grade = int(input('Input a number between 1 and 100: '))


if (student_level == 1) and (1 <= student_grade < 50):
    print("Fail")

elif (student_level == 1) and 50 <= student_grade <= 60:
    print("Pass")

elif (student_level == 1) and 61 <= student_grade <= 70:
    print("Merit")

elif (student_level == 1) and 71 <= student_grade <= 100:
    print("Distinction")

elif (student_level == 2) and (1 <= student_grade < 40):
    print("Fail")

elif (student_level == 2) and 40 > student_grade > 50:
    print("Pass")

elif (student_level == 2) and 51 <= student_grade <= 65:
    print("Merit")

elif (student_level == 2) and 66 <= student_grade <= 100:
    print("Distinction")

else:
    print("Error: marks must between 1 and 100")