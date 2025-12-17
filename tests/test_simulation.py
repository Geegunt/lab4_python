import pytest
from src.simulation import load_books_from_json
from src.book import Book, RareBook, DigitalBook


class TestSimulation:
    
    def test_load_books_from_json(self):
        books = load_books_from_json()
        assert len(books) == 10
        assert all(hasattr(b, 'isbn') for b in books)
    
    def test_loaded_books_have_correct_types(self):
        books = load_books_from_json()
        book_types = [type(b).__name__ for b in books]
        assert "Book" in book_types
        assert "RareBook" in book_types
        assert "DigitalBook" in book_types
    
    def test_loaded_books_have_required_attributes(self):
        books = load_books_from_json()
        for book in books:
            assert hasattr(book, 'title')
            assert hasattr(book, 'author')
            assert hasattr(book, 'year')
            assert hasattr(book, 'genre')
            assert hasattr(book, 'isbn')
    
    def test_rare_books_have_value(self):
        books = load_books_from_json()
        rare_books = [b for b in books if isinstance(b, RareBook)]
        assert len(rare_books) > 0
        for book in rare_books:
            assert hasattr(book, 'value')
            assert book.value > 0
    
    def test_digital_books_have_file_size(self):
        books = load_books_from_json()
        digital_books = [b for b in books if isinstance(b, DigitalBook)]
        assert len(digital_books) > 0
        for book in digital_books:
            assert hasattr(book, 'file_size_mb')
            assert book.file_size_mb > 0
