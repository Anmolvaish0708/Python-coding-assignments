# Week 1 Lab — Student Profile Card

Ask for a student's details, compute their result, and print a clean
profile card. Everything you need is from this week's classes: `input()`,
type casting, operators, and f-strings.

**Time: about an hour.** Work in `student_profile.py` — the three TODOs
are the whole lab.

## Tasks

1. **Collect details** (`collect_student`) — name, age, and marks in
   three subjects (out of 100 each). Remember: `input()` always gives you
   a string — cast age and marks to numbers.
2. **Compute the result** (`compute_results`) — total, percentage, and a
   grade: A for 90%+, B for 75%+, C for 50%+, otherwise "Needs work".
3. **Print the card** (`format_profile`) — use f-strings. Percentage must
   show exactly 2 decimal places.

## Expected output (roughly)

```
==============================
 STUDENT PROFILE
==============================
 Name       : Asha Verma
 Age        : 19
 Total      : 254 / 300
 Percentage : 84.67%
 Grade      : B
==============================
```

## Run it

```sh
python3 student_profile.py
```

Stuck? Ask the Layrs coach in the sidebar — then hit **Submit for
review** when your card prints correctly.
