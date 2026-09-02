from datetime import datetime


class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    def __str__(self):
        return f"{self.amount:.2f} | {self.category} | {self.date}"

    def to_file_format(self):
        return f"{self.amount:.2f}|{self.category}|{self.date}"

    @classmethod
    def from_file_format(cls, line):
        parts = line.strip().split("|")

        if len(parts) != 3:
            raise ValueError("Invalid expense record format.")

        amount = float(parts[0])
        category = parts[1]
        date = parts[2]

        datetime.strptime(date, "%Y-%m-%d")

        return cls(amount, category, date)