import pytest
from library_system import Book, BookGenre, MembershipLevel, BookNotAvailableError, LateReturnError, InvalidMembershipError, Member

# Test 1: Successful book borrow
def test_book_borrow():
    book = Book("1984", BookGenre.FICTION, True)
    book.borrow()
    assert book.is_available == False

# Test 2: Borrowing an unavailable book
def test_book_already_borrowed():
    book = Book("1984", BookGenre.FICTION, False)
    with pytest.raises(BookNotAvailableError):
        book.borrow()

# Test 3: Returning a book late
def test_book_return_late():
    book = Book("Sapiens", BookGenre.HISTORY, False)
    with pytest.raises(LateReturnError):
        book.return_book(is_late=True)

# Test 4: Returning a book on time
def test_book_return_on_time():
    book = Book("Sapiens", BookGenre.HISTORY, False)
    book.return_book(is_late=False)
    assert book.is_available == True

# Test 5: Membership fee for PREMIUM
def test_membership_fee_premium():
    member = Member("Alice", MembershipLevel.PREMIUM)
    assert member.get_fee() == 200

# Test 6: Membership fee for BASIC
def test_membership_fee_basic():
    member = Member("Bob", MembershipLevel.BASIC)
    assert member.get_fee() == 100

# Test 7: Invalid membership level
def test_invalid_membership():
    member = Member("Eve", "INVALID_LEVEL")
    with pytest.raises(InvalidMembershipError):
        member.get_fee()

# Test 8: Automatic values in BookGenre
def test_book_genre_values():
    assert BookGenre.FICTION.value == 1
    assert BookGenre.NON_FICTION.value == 2

# Test 9: Custom values in MembershipLevel
def test_membership_level_values():
    assert MembershipLevel.BASIC.value == 100
    assert MembershipLevel.PREMIUM.value == 200
    assert MembershipLevel.GOLD.value == 500

# Test 10: Borrow and return lifecycle
def test_borrow_and_return():
    book = Book("Cosmos", BookGenre.SCIENCE, True)
    book.borrow()
    assert book.is_available == False
    book.return_book(is_late=False)
    assert book.is_available == True