from book_manager import BookManager
from member_manager import MemberManager
from loan_manager import LoanManager
from exceptions import LoanNotFoundError


class Library:

    def __init__(self, name):
        self.name           = name
        self.book_manager   = BookManager()
        self.member_manager = MemberManager()
        self.loan_manager   = LoanManager()

    def add_book(self, title, author, isbn):
        self.book_manager.add_book(isbn, title, author)

    def remove_book(self, isbn):
        self.book_manager.remove_book(isbn)

    def search_books(self, query):
        return self.book_manager.search_books(query)

    def get_available_books(self):
        return self.book_manager.get_available_books()

    def register_member(self, name, member_id):
        self.member_manager.register_member(name, member_id)

    def get_all_members(self):
        return self.member_manager.get_all()

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
            raise LoanNotFoundError(
                f"{member.name} does not have book {isbn} on loan."
            )
        book.return_book()
        member.remove_loan(isbn)
        loan = self.loan_manager.get_active_for_book(isbn)
        if loan:
            loan.mark_returned()

    def get_status(self):
        books = self.book_manager.get_all()
        return {
            "name":      self.name,
            "total":     len(books),
            "available": sum(1 for b in books if b.is_available()),
            "borrowed":  sum(1 for b in books if not b.is_available()),
            "members":   len(self.member_manager.get_all())
        }

    def get_active_loans(self):
        result = []
        for loan in self.loan_manager.get_all():
            if not loan.returned:
                book   = self.book_manager.get_book(loan.isbn)
                member = self.member_manager.get_member(loan.member_id)
                result.append((book.title, member.name))
        return result

    def get_overdue(self):
        return self.loan_manager.get_overdue()