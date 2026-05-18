import json
from exceptions import BookNotAvailableError, BookAvailableError


class Book:
    """Represents a single book in the library."""

    def __init__(self, isbn, title, author):
        """Initialise a book as available.

        Args:
            isbn (str): Unique identifier for the book.
            title (str): Title of the book.
            author (str): Author of the book.
        """
        self.isbn      = isbn
        self.title     = title
        self.author    = author
        self.available = True

    def borrow(self):
        """Mark the book as borrowed.

        Raises:
            BookNotAvailableError: If the book is already borrowed.
        """
        if not self.available:
            raise BookNotAvailableError(
                f"{self.title} is not available."
            )
        self.available = False

    def return_book(self):
        """Mark the book as returned.

        Raises:
            BookAvailableError: If the book is already available.
        """
        if self.available:
            raise BookAvailableError(
                f"{self.title} is already available."
            )
        self.available = True

    def is_available(self):
        """Return True if the book is available for borrowing.

        Returns:
            bool: Availability status.
        """
        return self.available

    def to_dict(self):
        """Serialise the book to a dict for JSON storage.

        Returns:
            dict: Book data as a plain dictionary.
        """
        return {
            "isbn":      self.isbn,
            "title":     self.title,
            "author":    self.author,
            "available": self.available
        }

    @classmethod
    def from_dict(cls, data):
        """Deserialise a book from a dict loaded from JSON.

        Args:
            data (dict): Dictionary containing book fields.

        Returns:
            Book: A reconstructed Book instance.
        """
        book           = cls(data["isbn"], data["title"], data["author"])
        book.available = data["available"]
        return book

    def __str__(self):
        status = "available" if self.available else "borrowed"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) [{status}]"