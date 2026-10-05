# Worksheet 1.2: Task 1 Solution

import sys


inputted_grade_str = input("Enter your grade 0-100: ")

try:
    int_grade = int(inputted_grade_str)

    if int_grade < 0 or int_grade > 100:
        raise ValueError()
except ValueError:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if int_grade < 40:
    grade = "Fail"
elif int_grade < 70:
    grade = "Pass"
else:
    grade = "Distinction"

print(f"{int_grade} is a {grade}")
