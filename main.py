
from expenses import expense_menu
from attendance import attendance_menu
from grading import grading_menu
from billing import billing_menu
from reports import view_reports


def display_menu():

    print("\n==========================================")
    print(" EXPENSE ATTENDANCE GRADING BILLING SYSTEM")
    print("==========================================")

    print("1. Expense Management")
    print("2. Attendance Management")
    print("3. Grading System")
    print("4. Billing System")
    print("5. View Reports")
    print("6. Exit")

    print("------------------------------------------")


def main():

    while True:

        display_menu()

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            expense_menu()

        elif choice == "2":
            attendance_menu()

        elif choice == "3":
            grading_menu()

        elif choice == "4":
            billing_menu()

        elif choice == "5":
            view_reports()

        elif choice == "6":
            print("Thank you for using the system. Goodbye!")
            break

        else:
            print("Invalid choice. Enter 1-6.")


if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")
