import pytest
from models.member import Member


@pytest.fixture
def member():
    return Member("Alice", "M001")


# ── Loans ────────────────────────────────────────────────────────────

def test_new_member_has_no_loans(member):
    assert not member.has_loan("001")

def test_add_loan(member):
    member.add_loan("001")
    assert member.has_loan("001")

def test_remove_loan(member):
    member.add_loan("001")
    member.remove_loan("001")
    assert not member.has_loan("001")

def test_member_can_hold_multiple_loans(member):
    member.add_loan("001")
    member.add_loan("002")
    assert member.has_loan("001")
    assert member.has_loan("002")

def test_remove_loan_does_not_affect_others(member):
    member.add_loan("001")
    member.add_loan("002")
    member.remove_loan("001")
    assert not member.has_loan("001")
    assert member.has_loan("002")