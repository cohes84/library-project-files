import pytest
from library import Library


@pytest.fixture
def lib():
    library = Library("Test Library")
    library.add_book("Dune", "Herbert", "001")
    library.add_book("1984", "Orwell", "002")
    library.register_member("Alice", "M001")
    library.register_member("Bob",   "M002")
    return library


@pytest.fixture
def lib_with_loan(lib):
    lib.checkout("M001", "001")
    return lib


# ── Checkout ─────────────────────────────────────────────────────────

def test_checkout_returns_loan(lib):
    loan = lib.checkout("M001", "001")
    assert loan is not None
    assert loan.isbn      == "001"
    assert loan.member_id == "M001"
    assert loan.due_date  is not None

def test_checkout_makes_book_unavailable(lib):
    lib.checkout("M001", "001")
    available = [b.isbn for b in lib.get_available_books()]
    assert "001" not in available

def test_checkout_unavailable_raises(lib_with_loan):
    with pytest.raises(ValueError):
        lib_with_loan.checkout("M002", "001")

def test_checkout_unknown_member_raises(lib):
    with pytest.raises(KeyError):
        lib.checkout("UNKNOWN", "001")

def test_checkout_unknown_book_raises(lib):
    with pytest.raises(KeyError):
        lib.checkout("M001", "UNKNOWN")


# ── Return ───────────────────────────────────────────────────────────

def test_return_book_makes_available(lib_with_loan):
    lib_with_loan.return_book("M001", "001")
    available = [b.isbn for b in lib_with_loan.get_available_books()]
    assert "001" in available

def test_return_book_not_borrowed_raises(lib):
    with pytest.raises(ValueError):
        lib.return_book("M001", "001")


# ── Status ───────────────────────────────────────────────────────────

def test_status_total_books(lib):
    status = lib.get_status()
    assert status["total"] == 2

def test_status_available_decreases_on_checkout(lib):
    lib.checkout("M001", "001")
    status = lib.get_status()
    assert status["available"] == 1
    assert status["borrowed"]  == 1

def test_status_member_count(lib):
    status = lib.get_status()
    assert status["members"] == 2


# ── Active loans ─────────────────────────────────────────────────────

def test_active_loans_after_checkout(lib_with_loan):
    loans = lib_with_loan.get_active_loans()
    assert len(loans) == 1
    assert loans[0] == ("Dune", "Alice")

def test_active_loans_empty_initially(lib):
    assert lib.get_active_loans() == []


# ── Overdue ──────────────────────────────────────────────────────────

def test_no_overdue_on_fresh_checkout(lib):
    lib.checkout("M001", "001")
    assert lib.get_overdue() == []