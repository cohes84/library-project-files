from models.book_manager import BookManager
from models.member_manager import MemberManager
from models.loan_manager import LoanManager

class Library:

    def __init__(self, name):
        self.name           = name
        self.book_manager   = BookManager()
        self.member_manager = MemberManager()
        self.loan_manager   = LoanManager()

    # ── Books ──────────────────────────────────────────────
    def add_book(self, title, author, isbn):
        self.book_manager.add_book(isbn, title, author)

    def remove_book(self, isbn):
        self.book_manager.remove_book(isbn)

    def search_books(self, query):
        return self.book_manager.search_books(query)

    def get_available_books(self):
        return self.book_manager.get_available_books()

    def get_all_books(self):
        return self.book_manager.get_all()

    # ── Members ─────────────────────────────────────────────
    def register_member(self, name, member_id):
        self.member_manager.register_member(name, member_id)

    def get_all_members(self):
        return self.member_manager.get_all()

    # ── Transactions ────────────────────────────────────────
    def checkout(self, member_id, isbn):
        member = self.member_manager.get_member(member_id)
        book   = self.book_manager.get_book(isbn)
        book.borrow()
        member.add_loan(isbn)
        loan = self.loan_manager.create_loan(isbn, member_id)
        return loan

    def return_book(self, member_id, isbn):
        member = self.member_manager.get_member(member_id)
        book   = self.book_manager.get_book(isbn)
        if not member.has_loan(isbn):
            raise ValueError(f"{member.name} does not have book {isbn}")
        book.return_book()
        member.remove_loan(isbn)
        loan = self.loan_manager.get_active_for_book(isbn)
        if loan:
            loan.mark_returned()

    # ── Status ──────────────────────────────────────────────
    def get_status(self):
        total     = len(self.book_manager.get_all())
        available = len(self.book_manager.get_available_books())
        return {
            "name":      self.name,
            "total":     total,
            "available": available,
            "borrowed":  total - available,
            "members":   len(self.member_manager.get_all()),
        }

    def get_active_loans(self):
        result = []
        for book in self.book_manager.get_all():
            if not book.is_available():
                for member in self.member_manager.get_all():
                    if member.has_loan(book.isbn):
                        result.append((book.title, member.name))
        return result

    def get_overdue(self):
        return self.loan_manager.get_overdue()