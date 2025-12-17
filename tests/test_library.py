import pytest
from src.book import Book
from src.library import Library


class TestLibrary:
    
    def test_add_book_with_operator(self):
        library = Library()
        book = Book("Тест", "Автор", 2000, "Жанр", "978-0-0000-0001-1")
        library + book
        assert len(library.books) == 1
        assert book in library.books
    
    def test_sub_book_with_operator(self):
        library = Library()
        book = Book("Тест", "Автор", 2000, "Жанр", "978-0-0000-0001-1")
        library + book
        library - book
        assert len(library.books) == 0
    
    def test_call_search_by_author(self):
        library = Library()
        book = Book("Тест", "Иван Иванов", 2000, "Жанр", "978-0-0000-0001-1")
        library + book
        results = library("Иван Иванов")
        assert len(results) == 1
        assert results[0] == book
    
    def test_call_search_by_year(self):
        library = Library()
        book = Book("Тест", "Автор", 2000, "Жанр", "978-0-0000-0001-1")
        library + book
        results = library(2000)
        assert len(results) == 1
        assert results[0] == book
    
    def test_call_search_by_isbn(self):
        library = Library()
        book = Book("Тест", "Автор", 2000, "Жанр", "978-0-0000-0001-1")
        library + book
        result = library("978-0-0000-0001-1")
        assert result == book
    
    def test_call_search_by_genre(self):
        library = Library()
        book = Book("Тест", "Автор", 2000, "Фантастика", "978-0-0000-0001-1")
        library + book
        results = library("Фантастика", by_genre=True)
        assert len(results) == 1
        assert results[0] == book
    
    def test_call_search_not_found(self):
        library = Library()
        results = library("Несуществующий автор")
        assert results == []
    
    def test_chain_operations(self):
        library = Library()
        book1 = Book("Книга1", "Автор1", 2000, "Жанр", "978-0-0000-0001-1")
        book2 = Book("Книга2", "Автор2", 2001, "Жанр", "978-0-0000-0002-2")
        library + book1 + book2
        assert len(library.books) == 2
    
    def test_call_search_isbn_not_found(self):
        library = Library()
        result = library("978-0-0000-9999-9")
        assert result is None
    
    def test_sub_nonexistent_book_raises(self):
        library = Library()
        book = Book("Тест", "Автор", 2000, "Жанр", "978-0-0000-0001-1")
        with pytest.raises(ValueError):
            library - book
    
    def test_multiple_books_same_author(self):
        library = Library()
        book1 = Book("Книга1", "Толстой", 1869, "Роман", "978-0-0000-0001-1")
        book2 = Book("Книга2", "Толстой", 1877, "Роман", "978-0-0000-0002-2")
        library + book1 + book2
        results = library("Толстой")
        assert len(results) == 2
    
    def test_multiple_books_same_year(self):
        library = Library()
        book1 = Book("Книга1", "Автор1", 2000, "Роман", "978-0-0000-0001-1")
        book2 = Book("Книга2", "Автор2", 2000, "Драма", "978-0-0000-0002-2")
        library + book1 + book2
        results = library(2000)
        assert len(results) == 2
    
    @pytest.mark.parametrize("year", [1869, 1866, 1967])
    def test_search_various_years(self, year):
        library = Library()
        book = Book("Тест", "Автор", year, "Жанр", f"978-0-{year}-0001-1")
        library + book
        results = library(year)
        assert len(results) >= 1
