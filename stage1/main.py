class Book:

    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if not self.available:
            raise ValueError(f"Book {self.isbn} is not available.")
        self.available = False

    def return_book(self):
        if self.available:
            raise ValueError(f"Invalid return — book {self.isbn} is not borrowed.")
        self.available = True

    def is_available(self):
        return self.available

    def __str__(self):
        status = "available" if self.available else "borrowed"
        return f"{self.title} by {self.author} [{status}]"

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

from book import Book
from member import Member

class Library:

    def __init__(self, name):
        self.name = name
        self.books = []      # list of Book objects
        self.members = []    # list of Member objects

    def add_book(self, isbn, title, author):
        book = Book(isbn, title, author)
        self.books.append(book)
        print(f"Added: {title} by {author}")

    def register_member(self, name, member_id):
        if not member_id.startswith("M") or len(member_id) != 6:
            print(f"Invalid member ID: {member_id}")
            return
        member = Member(name, member_id)
        self.members.append(member)
        print(f"Registered: {name}")

    def find_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def find_member(self, member_id):
        for m in self.members:
            if m.member_id == member_id:
                return m
        return None

    def search_books(self, query):
        q = query.lower()
        return [b for b in self.books
                if q in b.title.lower() or q in b.author.lower()]

    def checkout(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)
        if not member or not book:
            print("Member or book not found.")
            return
        book.borrow()
        member.add_loan(isbn)
        print(f"{member.name} checked out {book.title}")

    def return_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)
        if not member or not book:
            print("Member or book not found.")
            return
        if not member.has_loan(isbn):
            raise ValueError(f"{member.name} does not have book {isbn}")
        book.return_book()
        member.remove_loan(isbn)
        print(f"Returned: {book.title}")

    def get_available_books(self):
        return [b for b in self.books if b.is_available()]

    def print_library_status(self):
        print(f"\n{'='*40}")
        print(f"  {self.name}")
        print(f"{'='*40}")
        total = len(self.books)
        available = sum(1 for b in self.books if b.is_available())
        print(f"  Books: {total} total, {available} available")
        print(f"  Members: {len(self.members)}")
        for b in self.books:
            if not b.is_available():
                for m in self.members:
                    if m.has_loan(b.isbn):
                        print(f"    {b.title} -> {m.name}")
        print(f"{'='*40}\n")