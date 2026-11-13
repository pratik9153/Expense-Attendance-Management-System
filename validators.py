
def get_int(prompt, min_val=None, max_val=None):

    while True:
        try:
            value = int(input(prompt))

            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}.")
                continue

            if max_val is not None and value > max_val:
                print(f"Value must not exceed {max_val}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Enter a whole number.")


def get_float(prompt, min_val=None, max_val=None):

    while True:
        try:
            value = float(input(prompt))

            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}.")
                continue

            if max_val is not None and value > max_val:
                print(f"Value must not exceed {max_val}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Enter a number.")


def get_name(prompt):

    while True:
        name = input(prompt).strip()

        if (2 <= len(name) <= 40 and
                all(ch.isalpha() or ch.isspace() for ch in name)):
            return name

        print("Name must contain 2-40 letters.")


def get_choice(prompt, options):

    while True:
        choice = input(prompt).strip().lower()

        for option in options:
            if choice == option.lower():
                return option

        print("Invalid choice. Choose from:", options)


def get_text(prompt):

    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty.")


def get_eval_int(prompt, min_val=None, max_val=None):

    while True:
        try:
            value = eval(input(prompt), {"__builtins__": {}}, {})

            if type(value) != int:
                print("Enter a whole number.")
                continue

            if min_val is not None and value < min_val:
                print(f"Minimum value is {min_val}.")
                continue

            if max_val is not None and value > max_val:
                print(f"Maximum value is {max_val}.")
                continue

            return value

        except (ValueError, SyntaxError, TypeError,
                NameError, ZeroDivisionError):
            print("Invalid input.")
