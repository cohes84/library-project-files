from book_manager import BookManager
from member_manager import MemberManager

class Library:

    def __init__(self, name):
        self.name = name
        self.book_manager = BookManager()
        self.member_manager = MemberManager()

    # ── Books ──────────────────────────────────────────────
    def add_book(self, title, author, isbn):
        try:
            self.book_manager.add_book(isbn, title, author)
            print(f"Added: {title} by {author}")
        except ValueError:
            print(f"Book {isbn} already exists.")
        except:
            print("Error")

    def remove_book(self, isbn):
        try:
            self.book_manager.remove_book(isbn)
            print(f"Removed: {isbn}")
        except KeyError:
            print(f"Book {isbn} not found.")
        except:
            print("Error")

    def search_books(self, query):
        try:
            results = self.book_manager.search_books(query)
            if not results:
                print("No books found.")
            for book in results:
                print(f"  {book}")
        except:
            print("Error")

    def get_available_books(self):
        try:
            books = self.book_manager.get_available_books()
            print(f"\n{self.name} — Available books:")
            for book in books:
                print(f"  {book}")
        except:
            print("Error")

    def get_all_books(self):
        try:
            books = self.book_manager.get_all()
            for book in books:
                print(f"  {book}")
        except:
            print("Error")

    # ── Members ─────────────────────────────────────────────
    def register_member(self, name, member_id):
        try:
            self.member_manager.register_member(name, member_id)
            print(f"Registered: {name}")
        except ValueError as e:
            print(f"Error: {e}")
        except:
            print("Error")

    def get_all_members(self):
        try:
            members = self.member_manager.get_all()
            for member in members:
                print(f"  {member}")
        except:
            print("Error")

    # ── Transactions ────────────────────────────────────────
    def checkout(self, member_id, isbn):
        try:
            member = self.member_manager.get_member(member_id)
            book   = self.book_manager.get_book(isbn)
            book.borrow()
            member.add_loan(isbn)
            print(f"{member.name} checked out {book.title}")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")
        except:
            print("Error")

    def return_book(self, member_id, isbn):
        try:
            member = self.member_manager.get_member(member_id)
            book   = self.book_manager.get_book(isbn)
            if not member.has_loan(isbn):
                raise ValueError(f"{member.name} does not have book {isbn}")
            book.return_book()
            member.remove_loan(isbn)
            print(f"Returned: {book.title}")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")
        except:
            print("Error")