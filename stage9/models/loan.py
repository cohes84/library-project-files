from datetime import date, timedelta
from exceptions import LoanNotFoundError


class Loan:

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

    def to_dict(self):
        return {
            "loan_id":   self.loan_id,
            "isbn":      self.isbn,
            "member_id": self.member_id,
            "loan_date": self.loan_date.isoformat(),
            "due_date":  self.due_date.isoformat(),
            "returned":  self.returned
        }

    @classmethod
    def from_dict(cls, data):
        loan           = cls(data["loan_id"], data["isbn"], data["member_id"])
        loan.loan_date = date.fromisoformat(data["loan_date"])
        loan.due_date  = date.fromisoformat(data["due_date"])
        loan.returned  = data["returned"]
        return loan

    def __str__(self):
        status = "OVERDUE" if self.is_overdue() else "active"
        return f"Loan {self.loan_id}: {self.isbn} [{status}] due {self.due_date}"