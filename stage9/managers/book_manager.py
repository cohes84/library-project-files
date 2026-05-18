import json
from models.book import Book
from exceptions import BookNotFoundError, BookAlreadyExistsError


class BookManager:

    FILE = "data/books.json"

    def __init__(self):
        self.books = {}
        self.load()

    def add_book(self, isbn, title, author):
        if isbn in self.books:
            raise BookAlreadyExistsError(f"Book {isbn} already exists.")
        self.books[isbn] = Book(isbn, title, author)
        self.save()

    def remove_book(self, isbn):
        if isbn not in self.books:
            raise BookNotFoundError(f"Book {isbn} not found.")
        del self.books[isbn]
        self.save()

    def get_book(self, isbn):
        if isbn not in self.books:
            raise BookNotFoundError(f"Book {isbn} not found.")
        return self.books[isbn]

    def get_available_books(self):
        return [b for b in self.books.values() if b.is_available()]

    def search_books(self, query):
        q = query.lower()
        return [b for b in self.books.values()
                if q in b.title.lower() or q in b.author.lower()]

    def get_all(self):
        return list(self.books.values())

    def save(self):
        with open(self.FILE, "w") as f:
            json.dump(
                [book.to_dict() for book in self.books.values()],
                f, indent=2
            )

    def load(self):
        try:
            with open(self.FILE, "r") as f:
                records = json.load(f)
                for data in records:
                    book = Book.from_dict(data)
                    self.books[book.isbn] = book
        except FileNotFoundError:
            pass