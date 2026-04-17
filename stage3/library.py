from book_manager import BookManager
from member_manager import MemberManager

class Library:

    def __init__(self, name):
        self.name = name
        self.book_manager = BookManager()
        self.member_manager = MemberManager()

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

    def return_book(self, member_id, isbn):
        member = self.member_manager.get_member(member_id)
        book   = self.book_manager.get_book(isbn)
        if not member.has_loan(isbn):
            raise ValueError(f"{member.name} does not have book {isbn}")
        book.return_book()
        member.remove_loan(isbn)