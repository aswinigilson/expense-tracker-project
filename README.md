# Expense Tracker

## Description

The Expense Tracker is a console-based Python application that allows users to record, view, and summarize their expenses by category.

The application stores expense records permanently in a text file and uses a modular structure to separate expense management, file operations, category summarization, and user interface logic.

## Features

* Add a new expense
* View all recorded expenses
* Summarize expenses by category
* Validate expense amount
* Validate expense category
* Validate dates in `YYYY-MM-DD` format
* Store expenses persistently in `data/expenses.txt`
* Handle invalid input and file errors

## Project Structure

```text
expense_tracker_project/
├── data/
│   └── expenses.txt
├── modules/
│   ├── __init__.py
│   ├── expense.py
│   ├── file_operations.py
│   └── category_summarizer.py
├── main.py
└── README.md
```

## How to Run

1. Open Command Prompt or VS Code terminal.
2. Navigate to the project folder.
3. Run:

```bash
python main.py
```

## Menu Options

```text
1. Add Expense
2. View Expenses
3. Summarize by Category
4. Exit
```

## Expense Format

Expenses are stored in the following format:

```text
Amount|Category|Date
```

Example:

```text
150.00|Groceries|2025-07-01
25.50|Transport|2025-07-02
75.20|Utilities|2025-07-05
50.75|Food|2025-07-08
```

## Technologies Used

* Python
* Object-Oriented Programming
* File Handling
* Regular Expressions
* Date Validation
* Exception Handling
* Modular Programming

## Requirements

* Python 3.x
* Python standard library only

## Author

Expense Tracker Project
