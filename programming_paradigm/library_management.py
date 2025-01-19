class Book:
    def __init__(self, title, author):
        """Initialize a new Book object with a title, author, and set as not checked out."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available again."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is available (not checked out)."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title. If it's available, mark it as checked out."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """Return a checked-out book by title and make it available."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """List all books that are available (not checked out)."""
        available_books = [str(book) for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books available.")

from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()            