class Member:

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.loans = []   # list of ISBNs

    def add_loan(self, isbn):
        self.loans.append(isbn)

    def remove_loan(self, isbn):
        if isbn not in self.loans:
            raise ValueError(f"Loan {isbn} not found for {self.name}")
        self.loans.remove(isbn)

    def has_loan(self, isbn):
        return isbn in self.loans

    def __str__(self):
        return f"{self.name} ({self.member_id}) — {len(self.loans)} active loans"