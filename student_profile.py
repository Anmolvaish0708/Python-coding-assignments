"""Week 1 Lab — Student Profile Card.

Collect a student's details, compute total/percentage/grade, and print a
formatted profile card. See README.md for the expected output.
"""

SUBJECTS = ["Physics", "Chemistry", "Maths"]
MAX_MARKS_PER_SUBJECT = 100


def collect_student():
    """Ask for the student's name, age, and marks in each subject.

    Returns a dict like:
      {"name": "Asha", "age": 19, "marks": [88.0, 76.5, 90.0]}

    Remember: input() returns a string — cast age to int and each mark
    to float.
    """
    # TODO(task 1): collect name, age, and one mark per subject in
    # SUBJECTS, with proper type casting.
    name = input("enter your name: ")
    age = int(input("enter your age: "))
    phy_mark = float(input("enter physics marks: "))
    chem_marks = float(input("enter chemistry marks: "))
    math_marks = float(input("enter math marks: "))

    marks = [phy_mark,chem_marks,math_marks]

    student_details = {
        "name": name,
        "age": age,
        "marks": marks
    }

    return student_details
  


def compute_results(marks):
    """Return (total, percentage, grade) for a list of marks.

    percentage is out of 100 across all subjects. Grade bands:
      90 and above -> "A", 75 and above -> "B", 50 and above -> "C",
      below 50 -> "Needs work"
    """
    # TODO(task 2): compute total and percentage with arithmetic
    # operators, then pick the grade with an if/elif chain.

    total = sum(marks)
    

    max_possible = len(marks)* MAX_MARKS_PER_SUBJECT
    percentage = (total/max_possible)*100

    
    if(percentage >= 90):
         grade = "A"
    elif(percentage >= 75):
        grade = "B"
    elif(percentage >= 50):
        grade = "C"
    else:
        grade = "Needs work"    

    return total,percentage,grade             
    


def format_profile(student, total, percentage, grade):
    """Return the profile card as a single string, built with f-strings.

    Requirements: percentage shows exactly 2 decimal places, and the
    card looks like the sample in README.md.
    """
    # TODO(task 3): build and return the card using f-strings.
    
    max_possible = len(student["marks"]) * MAX_MARKS_PER_SUBJECT
    return f"""==============================
 STUDENT PROFILE
==============================
 Name       : {student['name']}
 Age        : {student['age']}
 Total      : {int(total)} / {max_possible}
 Percentage : {percentage:.2f}%
 Grade      : {grade}
==============================="""


def main():
    student = collect_student()
    total, percentage, grade = compute_results(student["marks"])
    print(format_profile(student, total, percentage, grade))


if __name__ == "__main__":
    main()
