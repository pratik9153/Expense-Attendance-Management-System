
from validators import get_text, get_float, get_choice

categories = ("Food", "Travel", "Utilities", "Stationery", "Other")

expenses = []

category_totals = {
    category: 0.0 for category in categories
}


def add_expense():

    description = get_text("Enter description: ")

    category = get_choice(
        "Enter category (Food/Travel/Utilities/Stationery/Other): ",
        categories
    )

    amount = get_float("Enter amount: ", min_val=0.01)

    expense = {
        "description": description,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    category_totals[category] += amount

    print("Expense added successfully!")


def view_expenses():

    if not expenses:
        print("No expense records available.")
        return

    print("\n---------------- EXPENSE RECORDS ----------------")

    print(f"{'Description':<20}{'Category':<15}{'Amount':>12}")

    for expense in expenses:

        print(
            f"{expense['description']:<20}"
            f"{expense['category']:<15}"
            f"{expense['amount']:>12.2f}"
        )


def expense_summary():

    if not expenses:
        print("No expense records available.")
        return

    total = 0

    highest = expenses[0]
    lowest = expenses[0]

    for expense in expenses:

        total += expense["amount"]

        if expense["amount"] > highest["amount"]:
            highest = expense

        if expense["amount"] < lowest["amount"]:
            lowest = expense

    print("\n----------- CATEGORY-WISE SUMMARY -----------")

    for category, amount in category_totals.items():

        print(f"{category:<15}{amount:>12.2f}")

    print("---------------------------------------------")
    print(f"{'GRAND TOTAL':<15}{total:>12.2f}")

    print(
        f"Highest Expense: {highest['description']} "
        f"({highest['amount']:.2f})"
    )

    print(
        f"Lowest Expense: {lowest['description']} "
        f"({lowest['amount']:.2f})"
    )


def expense_menu():

    while True:

        print("\n--- EXPENSE MANAGEMENT ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Expense Summary")
        print("4. Back")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            expense_summary()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Enter 1-4.")
