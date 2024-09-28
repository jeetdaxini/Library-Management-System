import pytest
from Library import Library

# Test adding books to the library
def test_add_book():
    library = Library()
    library.add_book('978-3-16-148410-0', 'Test Book', 'Author', 2023)
    assert len(library.books) == 1
    assert library.books['978-3-16-148410-0'].title == 'Test Book'

# Test borrowing a book
def test_borrow_book():
    library = Library()
    library.add_book('978-3-16-148410-0', 'Test Book', 'Author', 2023)
    library.borrow_book('978-3-16-148410-0')
    assert library.books['978-3-16-148410-0'].is_borrowed is True

# Test borrowing a book that's already borrowed
def test_borrow_unavailable_book():
    library = Library()
    library.add_book('978-3-16-148410-0', 'Test Book', 'Author', 2023)
    library.borrow_book('978-3-16-148410-0')
    with pytest.raises(ValueError, match="Book is already borrowed"):
        library.borrow_book('978-3-16-148410-0')

# Test returning a borrowed book
def test_return_book():
    library = Library()
    library.add_book('978-3-16-148410-0', 'Test Book', 'Author', 2023)
    library.borrow_book('978-3-16-148410-0')
    library.return_book('978-3-16-148410-0')
    assert library.books['978-3-16-148410-0'].is_borrowed is False

# Test viewing available books
def test_view_available_books():
    library = Library()
    library.add_book('978-3-16-148410-0', 'Test Book', 'Author', 2023)
    library.add_book('978-1-23-456789-0', 'Second Book', 'Another Author', 2021)
    library.borrow_book('978-1-23-456789-0')
    available_books = library.view_available_books()
    assert len(available_books) == 1
    assert available_books[0].title == 'Test Book'
