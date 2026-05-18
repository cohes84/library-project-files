from exceptions import (
    BookNotAvailableError, BookAvailableError
)


class Book:

    def __init__(self, isbn, title, author):
        self.isbn      = isbn
        self.title     = title
        self.author    = author
        self.available = True

    def borrow(self):
        if not self.available:
            raise BookNotAvailableError(
                f"{self.title} is not available."
            )
        self.available = False

    def return_book(self):
        if self.available:
            raise BookAvailableError(
                f"{self.title} is already available."
            )
        self.available = True

    def is_available(self):
        return self.available

    def to_dict(self):
        return {
            "isbn":      self.isbn,
            "title":     self.title,
            "author":    self.author,
            "available": self.available
        }

    @classmethod
    def from_dict(cls, data):
        book           = cls(data["isbn"], data["title"], data["author"])
        book.available = data["available"]
        return book

    def __str__(self):
        status = "available" if self.available else "borrowed"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) [{status}]"