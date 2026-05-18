import json
from models.loan import Loan
from exceptions import LoanNotFoundError


class LoanManager:

    FILE = "data/loans.json"

    def __init__(self):
        self.loans   = {}
        self.next_id = 1
        self.load()

    def create_loan(self, isbn, member_id):
        loan = Loan(self.next_id, isbn, member_id)
        self.loans[self.next_id] = loan
        self.next_id += 1
        self.save()
        return loan

    def get_active_for_book(self, isbn):
        return next(
            (l for l in self.loans.values()
             if l.isbn == isbn and not l.returned),
            None
        )

    def get_overdue(self):
        return [l for l in self.loans.values() if l.is_overdue()]

    def get_all(self):
        return list(self.loans.values())

    def save(self):
        with open(self.FILE, "w") as f:
            json.dump(
                [loan.to_dict() for loan in self.loans.values()],
                f, indent=2
            )

    def load(self):
        try:
            with open(self.FILE, "r") as f:
                records = json.load(f)
                for data in records:
                    loan = Loan.from_dict(data)
                    self.loans[loan.loan_id] = loan
                if self.loans:
                    self.next_id = max(self.loans.keys()) + 1
        except FileNotFoundError:
            pass