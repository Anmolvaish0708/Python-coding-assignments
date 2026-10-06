# Week 3 Lab — File-Based Expense Tracker

An expense tracker that *remembers*: close it, reopen it, your expenses
are still there — and no input or broken file should ever show the user
a raw Python traceback.

**Time: 60–90 minutes.** Two files: `storage.py` (file I/O — your main
work) and `tracker.py` (the app — partially done).

## Tasks

1. **`storage.load_expenses()`** — read `expenses.json` and return the
   list. Missing file? Corrupt file? Return `[]` — catch the exceptions,
   don't crash.
2. **`storage.save_expenses(expenses)`** — write the list back as JSON.
3. **`tracker.add_expense()`** — ask for description and amount. Wrap
   the amount conversion in try/except: bad input gets a friendly
   message, not a ValueError traceback. Reject negative amounts.
4. **`tracker.show_summary()`** — total spent, count, and the largest
   single expense.

## Check yourself

```sh
python3 tracker.py     # add 2-3 expenses, quit
python3 tracker.py     # they should still be there
```

Then try entering `ten rupees` as an amount — friendly message, no
crash? Delete a bracket inside `expenses.json` and run again — still no
crash? That's the lab. **Submit for review** when all three pass.
