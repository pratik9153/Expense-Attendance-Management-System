
from expenses import expense_summary
from attendance import attendance_summary
from grading import class_summary
from billing import bills


def view_reports():

    while True:

        print("\n========== REPORTS MENU ==========")

        print("1. Expense Report")
        print("2. Attendance Report")
        print("3. Grading Report")
        print("4. Billing Report")
        print("5. Back")

        choice = input("Enter choice (1-5): ")

        if choice == "1":

            expense_summary()

        elif choice == "2":

            attendance_summary()

        elif choice == "3":

            class_summary()

        elif choice == "4":

            if not bills:
                print("No billing records available.")

            else:

                for invoice in bills:
                    print(
                        f"Bill: {invoice['bill_no']} | "
                        f"Customer: {invoice['customer']} | "
                        f"Total: {invoice['grand_total']:.2f}"
                    )

        elif choice == "5":
            break

        else:
            print("Invalid choice.")
