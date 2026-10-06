"""Week 3 Lab — Expense Tracker app.

Uses storage.py for persistence. The menu loop is done; implement
add_expense and show_summary.
"""

import storage


def add_expense(expenses):
    """Ask for a description and amount, append to the list, and save.

    The amount must be converted with try/except: on ValueError print a
    friendly message and return without adding. Negative amounts are
    rejected with a message too.
    """
    # TODO(task 3)
    description = input("Enter the description... ")


    while True:
        try:
            amount = float(input("Enter the amount... "))
        
        except ValueError:
            print("Invalid input! enter a valid amount")   
            continue 

        if amount < 0:
            print("You're entering a negative amount.... enter a valid amount!")
            continue
        
        break

    dic = {"desc": description, "amount": amount}
    expenses.append(dic)
    storage.save_expenses(expenses)
    print("Expense added!") 

def show_summary(expenses):
    """Print: total spent, number of expenses, and the largest one."""
    # TODO(task 4)
    if not expenses:
        print("No expenses yet! ")
        return

    amounts = [expense["amount"] for expense in expenses]

    total_spent = sum(amounts)

    number_of_expenses = len(amounts)

    max_expense = max(amounts)

    print(f"Total spent: ₹{total_spent:.2f}")
    print(f"Number of expenses: {number_of_expenses}")
    print(f"Largest expense: ₹{max_expense:.2f}")

def main():
    expenses = storage.load_expenses()
    print(f"Loaded {len(expenses)} expense(s).")

    while True:
        choice = input("\n1) Add  2) List  3) Summary  q) Quit: ").strip().lower()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            for e in expenses:
                print(f"  ₹{e['amount']:.2f}  {e['desc']}")
        elif choice == "3":
            show_summary(expenses)
        elif choice == "q":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
