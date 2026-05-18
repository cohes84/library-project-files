from exceptions import LoanNotFoundError


class Member:

    def __init__(self, name, member_id):
        self.name      = name
        self.member_id = member_id
        self.loans     = []

    def add_loan(self, isbn):
        self.loans.append(isbn)

    def remove_loan(self, isbn):
        if isbn not in self.loans:
            raise LoanNotFoundError(f"Member does not have loan for {isbn}.")
        self.loans.remove(isbn)

    def has_loan(self, isbn):
        return isbn in self.loans

    def to_dict(self):
        return {
            "name":      self.name,
            "member_id": self.member_id,
            "loans":     self.loans
        }

    @classmethod
    def from_dict(cls, data):
        member       = cls(data["name"], data["member_id"])
        member.loans = data["loans"]
        return member

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"