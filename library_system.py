from enum import Enum, auto

# Enumerations
class BookGenre(Enum):
    FICTION = auto()
    NON_FICTION = auto()
    SCIENCE = auto()
    HISTORY = auto()
    BIOGRAPHY = auto()


class MembershipLevel(Enum):
    BASIC = 100
    PREMIUM = 200
    GOLD = 500


# Custom Exceptions
class BookNotAvailableError(Exception):
    """Raised when the requested book is not available for borrowing."""
    pass


class InvalidMembershipError(Exception):
    """Raised when an invalid membership level is provided."""
    pass


class LateReturnError(Exception):
    """Raised when a book is returned late."""
    pass


# Book Class
class Book:
    """Represents a book in the library."""

    def __init__(self, title: str, genre: BookGenre, is_available: bool = True):
        """
        Initializes a book with a title, genre, and availability status.

        Args:
            title (str): The title of the book.
            genre (BookGenre): The genre of the book.
            is_available (bool): Indicates if the book is available for borrowing. Defaults to True.
        """
        self.title = title
        self.genre = genre
        self.is_available = is_available

    def borrow(self) -> None:
        """
        Marks the book as borrowed if it is available.

        Raises:
            BookNotAvailableError: If the book is not available for borrowing.
        """
        if not self.is_available:
            raise BookNotAvailableError(f"The book '{self.title}' is not available.")
        self.is_available = False

    def return_book(self, is_late: bool = False) -> None:
        """
        Marks the book as returned.

        Args:
            is_late (bool): Indicates if the book is returned late. Defaults to False.

        Raises:
            LateReturnError: If the book is returned late.
        """
        if is_late:
            raise LateReturnError(f"The book '{self.title}' was returned late.")
        self.is_available = True


# Member Class
class Member:
    """Represents a library member."""

    def __init__(self, name: str, membership_level):
        """
        Initializes a library member with a name and membership level.

        Args:
            name (str): The name of the member.
            membership_level (MembershipLevel): The membership level of the member.
        """
        self.name = name
        self.membership_level = membership_level

    def get_fee(self) -> int:
        """
        Returns the membership fee associated with the member's level.

        Raises:
            InvalidMembershipError: If the membership level is invalid.

        Returns:
            int: The fee for the membership level.
        """
        if not isinstance(self.membership_level, MembershipLevel):
            raise InvalidMembershipError(f"'{self.membership_level}' is not a valid MembershipLevel.")
        return self.membership_level.value


# Example Usage
if __name__ == "__main__":
    # Create books
    book1 = Book("The Great Gatsby", BookGenre.FICTION)
    book2 = Book("A Brief History of Time", BookGenre.SCIENCE)

    # Borrow a book
    try:
        book1.borrow()
        print(f"'{book1.title}' has been borrowed.")
    except BookNotAvailableError as e:
        print(e)

    # Return a book
    try:
        book1.return_book(is_late=True)
    except LateReturnError as e:
        print(e)

    # Create a member
    try:
        member = Member("Alice", MembershipLevel.PREMIUM)
        print(f"Membership fee for {member.name}: {member.get_fee()}")
    except InvalidMembershipError as e:
        print(e)
