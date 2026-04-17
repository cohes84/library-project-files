# test_batch.py
# Run this to verify that CLI separation is correct.
# No user input — all operations are scripted.
# If Library has print() calls, you will see unexpected output here.

from library import Library

def test_all():
    lib = Library("Test Library")

    # If Library prints, you will see output here — that means
    # the separation is not yet complete.
    lib.add_book("Dune",    "Herbert", "001")
    lib.add_book("1984",    "Orwell",  "002")
    lib.add_book("Sapiens", "Harari",  "003")

    lib.register_member("Alice", "M00001")
    lib.register_member("Bob",   "M00002")

    lib.checkout("M00001", "001")
    assert not lib.book_manager.get_book("001").is_available(), \
        "Book should be borrowed"
    assert lib.member_manager.get_member("M00001").has_loan("001"), \
        "Alice should have the loan"

    results = lib.search_books("orwell")
    assert len(results) == 1, "Search should find 1984"

    lib.return_book("M00001", "001")
    assert lib.book_manager.get_book("001").is_available(), \
        "Book should be available again"

    try:
        lib.checkout("M00001", "999")
        assert False, "Should have raised KeyError"
    except KeyError:
        pass

    print("All tests passed.")


if __name__ == "__main__":
    test_all()