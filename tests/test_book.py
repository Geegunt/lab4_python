import pytest
from src.book import Book, RareBook, DigitalBook


class TestBook:
    
    def test_create_book(self):
        book = Book("Война и мир", "Лев Толстой", 1869, "Роман", "978-5-0001-0001-1")
        assert book.title == "Война и мир"
        assert book.author == "Лев Толстой"
        assert book.year == 1869
        assert book.genre == "Роман"
        assert book.isbn == "978-5-0001-0001-1"
    
    def test_book_repr(self):
        book = Book("Война и мир", "Лев Толстой", 1869, "Роман", "978-5-0001-0001-1")
        assert "Война и мир" in repr(book)
        assert "Лев Толстой" in repr(book)
    
    def test_book_equality(self):
        book1 = Book("Война и мир", "Лев Толстой", 1869, "Роман", "978-5-0001-0001-1")
        book2 = Book("Война и мир", "Лев Толстой", 1869, "Роман", "978-5-0001-0001-1")
        book3 = Book("Другая книга", "Автор", 2000, "Жанр", "978-5-0001-0002-2")
        assert book1 == book2
        assert book1 != book3


class TestRareBook:
    
    def test_create_rare_book(self):
        book = RareBook("Редкая", "Автор", 1800, "Жанр", "978-1-1111-1111-1", 50000.0)
        assert book.title == "Редкая"
        assert book.value == 50000.0
    
    def test_rare_book_repr(self):
        book = RareBook("Редкая", "Автор", 1800, "Жанр", "978-1-1111-1111-1", 50000.0)
        assert "Редкая" in repr(book)
        assert "50000" in repr(book)


class TestDigitalBook:
    
    def test_create_digital_book(self):
        book = DigitalBook("Электронная", "Автор", 2020, "Жанр", "978-2-2222-2222-2", 2.5)
        assert book.title == "Электронная"
        assert book.file_size_mb == 2.5
    
    def test_digital_book_repr(self):
        book = DigitalBook("Электронная", "Автор", 2020, "Жанр", "978-2-2222-2222-2", 2.5)
        assert "Электронная" in repr(book)
        assert "2.5" in repr(book)
