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