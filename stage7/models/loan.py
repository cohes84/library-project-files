from datetime import date, timedelta

class Loan:
    """Represents a single borrowing event."""

    LOAN_DAYS = 14

    def __init__(self, loan_id, isbn, member_id):
        self.loan_id   = loan_id
        self.isbn      = isbn
        self.member_id = member_id
        self.loan_date = date.today()
        self.due_date  = self.loan_date + timedelta(days=Loan.LOAN_DAYS)
        self.returned  = False

    def mark_returned(self):
        self.returned = True

    def is_overdue(self):
        return not self.returned and date.today() > self.due_date

    def __str__(self):
        status = "returned" if self.returned else (
            "OVERDUE" if self.is_overdue() else "active"
        )
        return f"Loan {self.loan_id}: {self.isbn} [{status}] due {self.due_date}"