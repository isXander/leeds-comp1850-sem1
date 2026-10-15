# Worksheet 1.3: Task 3

import csv

# Your code for the overall grade classification
def classify_grade(grade):
    if grade >= 70:
        return "1"
    elif grade >= 60:
        return "2:1"
    elif grade >= 50:
        return "2:2"
    elif grade >= 40:
        return "3"
    else:
        return "F"

# ask for filename of the student file
file_name = input("File name of student file? ")

calculated_data = []

# open the file
with open(file_name, 'r') as file:
    data = csv.reader(file)

    # skip header
    next(data)

    # read in the data, and for each student calculate their average grade and classification
    for row in data:
        student_id = row[0]
        grades = [int(grade) for grade in row[1:] if grade]
        average_grade = sum(grades) / len(grades)
        classification = classify_grade(average_grade)
        calculated_data.append([student_id, f"{average_grade:.2f}", classification])


# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}
with open(f"{file_name}_out.csv", 'w') as file:
   writer = csv.writer(file)
   writer.writerows(calculated_data)


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder
