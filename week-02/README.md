# Week 2 Lab — Student Record Manager

A tiny records system: add, find, update, and delete students, stored in
a dictionary. The menu loop is already written — your job is the four
functions it calls.

**Time: 60–90 minutes.** Work in `records.py`.

## Tasks

1. **add_student(students, roll, name, marks)** — insert a record. If
   the roll number already exists, don't overwrite — report it instead.
2. **find_student(students, roll)** — return the record, or `None` if
   the roll number doesn't exist (no crashes!).
3. **update_marks(students, roll, marks)** — change an existing
   student's marks; handle a missing roll number gracefully.
4. **delete_student(students, roll)** — remove a record; same care for
   missing roll numbers.

Design rule for all four: **return values, don't print** — the menu code
does the printing. That separation is the habit this lab builds.

## Run it

```sh
python3 records.py
```

Try: add two students, search one, update marks, delete, search again.
Then **Submit for review**.
