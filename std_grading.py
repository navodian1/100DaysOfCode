# we can calculate grades of student using function or directly from if else condition
# main purpose of this program is to understand working for dictionaries
"""

student_marks = {"rahul": 91, "raj": 85, "somya": 95, "varun": 71, "aniket": 46, "aarti": 56, "harry": 34}
student_grades = {}
for student in student_marks:
    marks = student_marks[student]
    if marks > 90:
        student_grades[student] = "A+"
    elif marks > 80:
        student_grades[student] = "A"
    elif marks > 70:
        student_grades[student] = "B+"
    elif marks > 60:
        student_grades[student] = "B"
    elif marks > 50:
        student_grades[student] = "C+"
    elif marks > 40:
        student_grades[student] = "C"
    else:
        student_grades[student] = "D"
print(student_grades)

"""


def student_grades(marks):
    grade_ranges = {
        (90, 100): 'A+',
        (80, 90): 'A',
        (70, 80): 'B+',
        (60, 70): 'B',
        (50, 60): 'C+',
        (40, 50): 'C',
        (0, 40): 'D'
    }

    for (lower, upper), grade in grade_ranges.items():
        if lower <= marks <= upper:
            return grade

    return 'Invalid input'


def main():
    try:
        student_marks = float(input("Enter the marks obtained by the student: "))
        if 0 <= student_marks <= 100:
            grade = student_grades(student_marks)
            print(f"The student's grade is: {grade}")
        else:
            print("Invalid input! Marks should be between 0 and 100.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")


if __name__ == "__main__":
    main()
