from .expense import Expense

FILE_PATH = "data/expenses.txt"


def read_expenses():
    expenses = []

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    try:
                        expense = Expense.from_file_format(line)
                        expenses.append(expense)
                    except ValueError:
                        continue

    except FileNotFoundError:
        return []

    except PermissionError:
        raise PermissionError("Permission denied while reading expenses.txt.")

    except OSError as error:
        raise OSError(f"File reading error: {error}")

    return expenses


def append_expense(expense):
    try:
        with open(FILE_PATH, "a", encoding="utf-8") as file:
            file.write(expense.to_file_format() + "\n")

    except PermissionError:
        raise PermissionError("Permission denied while writing to expenses.txt.")

    except OSError as error:
        raise OSError(f"File writing error: {error}")