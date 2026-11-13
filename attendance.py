
from validators import get_eval_int, get_int, get_name

attendance = {}

total_working_days = 0


def attendance_percentage(present, total):

    return (present / total) * 100


def attendance_status(percentage):

    if percentage >= 75:
        return "Eligible"

    elif percentage >= 60:
        return "Warning"

    else:
        return "Shortage"


def mark_attendance():

    global total_working_days

    if total_working_days == 0:

        total_working_days = get_eval_int(
            "Enter total working days: ", 1
        )

    number = get_int("Enter number of students: ", 1)

    for i in range(number):

        print(f"\nStudent {i + 1}")

        while True:

            try:
                rollno, name = map(
                    str.strip,
                    input("Enter Roll No and Name (comma separated): ").split(",", 1)
                )

            except ValueError:
                print("Enter roll number and name separated by comma.")
                continue

            if not rollno or not name:
                print("Both fields are required.")

            elif rollno in attendance:
                print("Roll number already exists.")

            else:
                break

        present = get_eval_int(
            "Enter days present: ",
            0,
            total_working_days
        )

        percentage = attendance_percentage(
            present, total_working_days
        )

        status = attendance_status(percentage)

        attendance[rollno] = {
            "name": name,
            "total_days": total_working_days,
            "present": present,
            "percentage": percentage,
            "status": status
        }

        print("Attendance recorded successfully!")


def attendance_summary():

    if not attendance:
        print("No attendance records available.")
        return

    print("\n---------------- ATTENDANCE REPORT ----------------")

    print(
        f"{'Roll No':<12}{'Name':<15}"
        f"{'Total':<10}{'Present':<10}"
        f"{'Percentage':<13}{'Status'}"
    )

    total_percentage = 0

    highest = next(iter(attendance))
    lowest = next(iter(attendance))

    status_count = {
        "Eligible": 0,
        "Warning": 0,
        "Shortage": 0
    }

    for rollno, details in attendance.items():

        percentage = details["percentage"]

        print(
            f"{rollno:<12}"
            f"{details['name']:<15}"
            f"{details['total_days']:<10}"
            f"{details['present']:<10}"
            f"{percentage:<13.2f}"
            f"{details['status']}"
        )

        total_percentage += percentage

        if percentage > attendance[highest]["percentage"]:
            highest = rollno

        if percentage < attendance[lowest]["percentage"]:
            lowest = rollno

        status_count[details["status"]] += 1

    average = total_percentage / len(attendance)

    print("\n--------------- ATTENDANCE SUMMARY ---------------")

    print("Total Students:", len(attendance))
    print(f"Average Attendance: {average:.2f}%")

    print(
        f"Highest: {attendance[highest]['name']} "
        f"({attendance[highest]['percentage']:.2f}%)"
    )

    print(
        f"Lowest: {attendance[lowest]['name']} "
        f"({attendance[lowest]['percentage']:.2f}%)"
    )

    print("Eligible:", status_count["Eligible"])
    print("Warning:", status_count["Warning"])
    print("Shortage:", status_count["Shortage"])


def attendance_menu():

    while True:

        print("\n--- ATTENDANCE MANAGEMENT ---")
        print("1. Mark Attendance")
        print("2. Attendance Summary")
        print("3. Back")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            mark_attendance()

        elif choice == "2":
            attendance_summary()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")
