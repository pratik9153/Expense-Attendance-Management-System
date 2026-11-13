
import logging
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import expenses
import attendance
import grading
import billing

logging.basicConfig(
    filename=Path(__file__).parent / "test_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)


def test_case(test_id, description, condition):
    if condition:
        logging.info("%s - %s - PASS", test_id, description)
        print(test_id, "PASS")
    else:
        logging.error("%s - %s - FAIL", test_id, description)
        print(test_id, "FAIL")


# TC-04: Expense calculation
test_case(
    "TC-04",
    "Expense amount validation",
    expenses.get_float.__name__ == "get_float"
)

# TC-07: Attendance percentage
test_case(
    "TC-07",
    "75 percent attendance",
    attendance.attendance_status(
        attendance.attendance_percentage(30, 40)
    ) == "Eligible"
)

# TC-08: Attendance warning
test_case(
    "TC-08",
    "72.5 percent attendance",
    attendance.attendance_status(
        attendance.attendance_percentage(29, 40)
    ) == "Warning"
)

# TC-09: Attendance shortage
test_case(
    "TC-09",
    "50 percent attendance",
    attendance.attendance_status(
        attendance.attendance_percentage(20, 40)
    ) == "Shortage"
)

# TC-12: Grade A+
test_case(
    "TC-12",
    "90 percent grade",
    grading.calculate_grade(90)[0] == "A+"
)

# TC-13: Grade F
test_case(
    "TC-13",
    "34 percent grade",
    grading.calculate_grade(34)[0] == "F"
)

# TC-16: Billing total
subtotal = 500
tax = billing.calculate_tax(subtotal)

test_case(
    "TC-16",
    "18 percent tax calculation",
    subtotal + tax == 590
)

# TC-17: Discount calculation
test_case(
    "TC-17",
    "5 percent discount",
    billing.calculate_discount(1000) == 0.05
)

print("\nTesting completed.")
print("Check tests/test_log.txt for results.")
