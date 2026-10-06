"""Storage module — ALL file reading/writing for the tracker lives here.

The app (tracker.py) imports these two functions and never touches the
file itself. That separation is the point of this module.
"""

import json

EXPENSES_FILE = "expenses.json"


def load_expenses():
    """Return the list of expense dicts from EXPENSES_FILE.

    Each expense looks like: {"desc": "chai", "amount": 15.0}

    Must NOT crash if the file is missing (first run) or corrupt —
    catch FileNotFoundError and json.JSONDecodeError and return [].
    """
    # TODO(task 1)
    try:
        with open(EXPENSES_FILE, "r") as f:
            data = json.load(f)
        return data    
    except (FileNotFoundError, json.JSONDecodeError):
        data = []    
        return data


def save_expenses(expenses):
    """Write the list of expenses to EXPENSES_FILE as JSON."""
    # TODO(task 2)
    with open(EXPENSES_FILE, "w") as f:
        json.dump(expenses, f, indent=4)
