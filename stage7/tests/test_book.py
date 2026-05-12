import pytest
from models.book import Book


@pytest.fixture
def book():
    return Book("001", "Dune", "Herbert")


@pytest.fixture
def borrowed_book():
    b = Book("001", "Dune", "Herbert")
    b.borrow()
    return b


# ── Availability ────────────────────────────────────────────────────

def test_new_book_is_available(book):
    assert book.is_available()

def test_borrow_makes_unavailable(book):
    book.borrow()
    assert not book.is_available()

def test_return_makes_available(borrowed_book):
    borrowed_book.return_book()
    assert borrowed_book.is_available()


# ── Errors ──────────────────────────────────────────────────────────

def test_borrow_unavailable_raises(borrowed_book):
    with pytest.raises(ValueError):
        borrowed_book.borrow()

def test_return_available_raises(book):
    with pytest.raises(ValueError):
        book.return_book()