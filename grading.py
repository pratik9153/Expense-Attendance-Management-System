
from validators import get_name, get_float

subjects = ["Maths", "Science", "English", "History", "Computer"]

students = {}


def calculate_grade(percentage):

    if percentage >= 90:
        return "A+", "Outstanding"

    elif percentage >= 80:
        return "A", "Excellent"

    elif percentage >= 70:
        return "B", "Very Good"

    elif percentage >= 60:
        return "C", "Good"

    elif percentage >= 50:
        return "D", "Satisfactory"

    elif percentage >= 35:
        return "E", "Pass"

    else:
        return "F", "Fail"


def add_student():

    name = get_name("Enter student name: ")

    if name in students:
        print("Student already exists.")
        return

    marks = {}

    for subject in subjects:

        mark = get_float(
            f"Enter {subject} marks: ", 0, 100
        )

        marks[subject] = mark

    total = sum(marks.values())

    average = total / len(subjects)

    percentage = (total / (len(subjects) * 100)) * 100

    grade, remark = calculate_grade(percentage)

    if any(mark < 35 for mark in marks.values()):
        result = "FAIL"
    else:
        result = "PASS"

    students[name] = {
        "marks": marks,
        "total": total,
        "average": average,
        "percentage": percentage,
        "grade": grade,
        "remark": remark,
        "result": result
    }

    print("Student marks added successfully!")


def generate_report_card():

    if not students:
        print("No student records available.")
        return

    for name, details in students.items():

        print("\n========== REPORT CARD ==========")

        print("Student:", name)

        print("---------------------------------")
        print(f"{'Subject':<20}{'Marks':>10}")

        for subject, mark in details["marks"].items():

            print(f"{subject:<20}{mark:>10.2f}")

        print("---------------------------------")

        print(f"Total: {details['total']:.2f}/500")
        print(f"Average: {details['average']:.2f}")
        print(f"Percentage: {details['percentage']:.2f}%")
        print(f"Grade: {details['grade']}")
        print(f"Remark: {details['remark']}")
        print(f"Result: {details['result']}")

        print("=================================")


def class_summary():

    if not students:
        print("No student records available.")
        return

    total_percentage = 0

    topper = next(iter(students))

    pass_count = 0
    fail_count = 0

    for name, details in students.items():

        total_percentage += details["percentage"]

        if details["percentage"] > students[topper]["percentage"]:
            topper = name

        if details["result"] == "PASS":
            pass_count += 1

        else:
            fail_count += 1

    class_average = total_percentage / len(students)

    print("\n----------- CLASS SUMMARY -----------")

    print("Total Students:", len(students))

    print(f"Class Average: {class_average:.2f}%")

    print(
        f"Topper: {topper} "
        f"({students[topper]['percentage']:.2f}%)"
    )

    print("Pass Count:", pass_count)
    print("Fail Count:", fail_count)


def grading_menu():

    while True:

        print("\n--- GRADING SYSTEM ---")
        print("1. Add Student Marks")
        print("2. Generate Report Cards")
        print("3. Class Summary")
        print("4. Back")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            generate_report_card()

        elif choice == "3":
            class_summary()

        elif choice == "4":
            break

        else:
            print("Invalid choice.")
