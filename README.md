# Expense & Attendance Management System

A Python-based, console-driven application that manages expenses, student attendance, academic grading, and billing through a menu-driven interface.

## Features

### 1. Expense Management
- Add expenses with description, category, and amount.
- Supported categories: Food, Travel, Utilities, Stationery, and Other.
- View all expense records.
- Calculate category-wise expenses and grand total.
- Identify highest and lowest expenses.

### 2. Attendance Management
- Record student attendance using unique roll numbers.
- Store attendance records using dictionaries.
- Calculate attendance percentages.
- Classify attendance status:
  - Eligible: 75% or above
  - Warning: 60% to below 75%
  - Shortage: Below 60%
- Generate attendance summaries.
- Identify students with the highest and lowest attendance.

### 3. Grading System
- Manage marks for five subjects:
  - Maths
  - Science
  - English
  - History
  - Computer
- Calculate total marks, average, and percentage.
- Assign grades from A+ to F.
- Generate student report cards.
- Generate class performance summaries.

### 4. Billing System
- Generate customer invoices.
- Add multiple items with unit prices and quantities.
- Apply discount slabs based on subtotal.
- Calculate 18% tax after discount.
- Generate invoices with the final payable amount.

### 5. Reports
- Expense reports
- Attendance reports
- Grading reports
- Billing reports

## Technologies Used

- Python 3.8+
- Dictionaries and Lists
- Functions and Modules
- Loops and Conditional Statements
- Exception Handling
- CSV
- Logging Module
- Python Standard Library

## Project Structure

```text
Expense & Attendance Management System/
│
├── main.py
├── validators.py
├── expenses.py
├── attendance.py
├── grading.py
├── billing.py
├── reports.py
│
├── tests/
│   ├── test_cases.csv
│   ├── run_tests.py
│   └── test_log.txt
│
└── README.md
```

## Testing

The project includes test cases to verify the functionality of different modules.

- **test_cases.csv:** Contains 20 test scenarios with inputs and expected results.
- **run_tests.py:** Executes selected automated function-level checks.
- **test_log.txt:** Stores test execution results using Python's built-in logging module, including timestamps and PASS/FAIL status.

The current automated test script performs 8 selected function-level checks.

## Installation and Execution

**1. Clone the repository**

```bash
git clone https://github.com/pratik9153/Expense-Attendance-Management-System.git
```

**2. Navigate to the project directory**

```bash
cd Expense-Attendance-Management-System
```

**3. Run the application**

```bash
python main.py
```

**4. Run automated checks**

```bash
python tests/run_tests.py
```

## Application Menu

The application provides the following main menu:

1. Expense Management
2. Attendance Management
3. Grading System
4. Billing System
5. View Reports
6. Exit

## Author

**Pratik Choudhary**

GitHub: [https://github.com/pratik9153](https://github.com/pratik9153)

---

This project was developed as a Python programming project to demonstrate modular programming, data structures, input validation, console-based application development, and basic automated testing.