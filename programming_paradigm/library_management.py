class Book:
    """Represents a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """Represents a library that manages a collection of books."""

    def __init__(self):
        self._books = []  # private list of Book instances

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title (make it unavailable)."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        """Return a book by title (make it available)."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        """Print all available books."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
