from loan import Loan

class LoanManager:

    def __init__(self):
        self.loans   = {}   # loan_id: Loan
        self.next_id = 1

    def create_loan(self, isbn, member_id):
        loan = Loan(self.next_id, isbn, member_id)
        self.loans[self.next_id] = loan
        self.next_id += 1
        return loan

    def get_loan(self, loan_id):
        if loan_id not in self.loans:
            raise KeyError(f"Loan {loan_id} not found.")
        return self.loans[loan_id]

    def get_active_for_member(self, member_id):
        return [l for l in self.loans.values()
                if l.member_id == member_id and not l.returned]

    def get_active_for_book(self, isbn):
        for l in self.loans.values():
            if l.isbn == isbn and not l.returned:
                return l
        return None

    def get_overdue(self):
        return [l for l in self.loans.values() if l.is_overdue()]

    def get_all(self):
        return list(self.loans.values())