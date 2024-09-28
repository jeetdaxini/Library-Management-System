class Book:
    """A class representing a book in the library."""
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def __repr__(self):
        return f"{self.title} by {self.author} ({self.year})"


class Library:
    """A class representing the library with various operations."""
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, year):
        """Add a new book to the library."""
        if isbn in self.books:
            raise ValueError("Book with this ISBN already exists.")
        new_book = Book(isbn, title, author, year)
        self.books[isbn] = new_book

    def borrow_book(self, isbn):
        """Borrow a book from the library."""
        if isbn not in self.books:
            raise ValueError("Book not found.")
        if self.books[isbn].is_borrowed:
            raise ValueError("Book is already borrowed.")
        self.books[isbn].is_borrowed = True

    def return_book(self, isbn):
        """Return a borrowed book."""
        if isbn not in self.books:
            raise ValueError("Book not found.")
        if not self.books[isbn].is_borrowed:
            raise ValueError("Book is not borrowed.")
        self.books[isbn].is_borrowed = False

    def view_available_books(self):
        """View all available books in the library."""
        return [book for book in self.books.values() if not book.is_borrowed]
