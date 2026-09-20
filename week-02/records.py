"""Week 2 Lab — Student Record Manager.

Records live in a dict keyed by roll number:
    students = {
        "101": {"name": "Asha", "marks": 88.5},
        ...
    }

Implement the four functions below. The menu loop at the bottom is done
for you — it calls your functions and prints what they return.
"""


def add_student(students, roll, name, marks):
    """Insert a new record. Return True if added, False if the roll
    number already exists (do NOT overwrite an existing student)."""
    # TODO(task 1)
    if roll not in students.keys():
        students[roll] = {
            "name": name,
            "marks": marks
        }
        return True
    else:
        return False

       


def find_student(students, roll):
    """Return the record dict for this roll number, or None if absent."""
    # TODO(task 2)
    return students.get(roll, None)


def update_marks(students, roll, marks):
    """Update an existing student's marks. Return True on success,
    False if the roll number doesn't exist."""
    # TODO(task 3)
    if roll in students.keys():
        students[roll]["marks"]=marks
        return True
    else:
        return False


def delete_student(students, roll):
    """Remove the record. Return True on success, False if absent."""
    # TODO(task 4)
    if roll in students.keys():
        del students[roll]
        return True
    else:
        return False


# ---------------------------------------------------------------------
# Menu loop — already complete. Read it; you'll write one like it soon.
# ---------------------------------------------------------------------

MENU = """
1) Add student   2) Find student   3) Update marks
4) Delete        5) List all       q) Quit
"""


def main():
    students = {}
    while True:
        print(MENU)
        choice = input("Choose: ").strip().lower()
        if choice == "1":
            roll = input("Roll no: ").strip()
            name = input("Name: ").strip()
            marks = float(input("Marks: "))
            ok = add_student(students, roll, name, marks)
            print("Added." if ok else "That roll number already exists.")
        elif choice == "2":
            record = find_student(students, input("Roll no: ").strip())
            print(record if record else "No such student.")
        elif choice == "3":
            roll = input("Roll no: ").strip()
            marks = float(input("New marks: "))
            ok = update_marks(students, roll, marks)
            print("Updated." if ok else "No such student.")
        elif choice == "4":
            ok = delete_student(students, input("Roll no: ").strip())
            print("Deleted." if ok else "No such student.")
        elif choice == "5":
            for roll, rec in students.items():
                print(f"{roll}: {rec['name']} — {rec['marks']}")
        elif choice == "q":
            print("Bye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
