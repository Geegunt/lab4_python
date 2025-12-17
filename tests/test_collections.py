import pytest
from src.book import Book
from src.book_collection import BookCollection
from src.index_dict import IndexDict


class TestBookCollection:
    
    def test_add_and_len(self):
        collection = BookCollection()
        book = Book("Тест", "Автор", 2000, "Жанр", "978-0-0000-0001-1")
        collection.add_book(book)
        assert len(collection) == 1
    
    def test_contains(self):
        collection = BookCollection()
        book = Book("Тест", "Автор", 2000, "Жанр", "978-0-0000-0001-1")
        collection.add_book(book)
        assert book in collection
    
    def test_getitem(self):
        collection = BookCollection()
        book = Book("Тест", "Автор", 2000, "Жанр", "978-0-0000-0001-1")
        collection.add_book(book)
        assert collection[0] == book
    
    def test_iter(self):
        collection = BookCollection()
        book1 = Book("Книга1", "Автор", 2000, "Жанр", "978-0-0000-0001-1")
        book2 = Book("Книга2", "Автор", 2001, "Жанр", "978-0-0000-0002-2")
        collection.add_book(book1)
        collection.add_book(book2)
        books = list(collection)
        assert len(books) == 2


class TestIndexDict:
    
    def test_add_and_len(self):
        index = IndexDict()
        book = Book("Тест", "Автор", 2000, "Жанр", "978-0-0000-0001-1")
        index.add_book(book)
        assert len(index) == 1
    
    def test_contains(self):
        index = IndexDict()
        book = Book("Тест", "Автор", 2000, "Жанр", "978-0-0000-0001-1")
        index.add_book(book)
        assert "978-0-0000-0001-1" in index
        assert "978-0-0000-0002-2" not in index
    
    def test_getitem(self):
        index = IndexDict()
        book = Book("Тест", "Автор", 2000, "Жанр", "978-0-0000-0001-1")
        index.add_book(book)
        assert index["978-0-0000-0001-1"] == book
    
    def test_get_by_author(self):
        index = IndexDict()
        book = Book("Тест", "Иван Иванов", 2000, "Жанр", "978-0-0000-0001-1")
        index.add_book(book)
        results = index.get_by_author("Иван Иванов")
        assert len(results) == 1
    
    def test_get_by_year(self):
        index = IndexDict()
        book = Book("Тест", "Автор", 2000, "Жанр", "978-0-0000-0001-1")
        index.add_book(book)
        results = index.get_by_year(2000)
        assert len(results) == 1
    
    def test_remove_book(self):
        index = IndexDict()
        book = Book("Тест", "Автор", 2000, "Жанр", "978-0-0000-0001-1")
        index.add_book(book)
        index.remove_book(book)
        assert len(index) == 0
        assert "978-0-0000-0001-1" not in index
    
    def test_getitem_raises_keyerror(self):
        index = IndexDict()
        with pytest.raises(KeyError):
            _ = index["978-0-0000-9999-9"]
    
    def test_iter(self):
        index = IndexDict()
        book1 = Book("Книга1", "Автор", 2000, "Жанр", "978-0-0000-0001-1")
        book2 = Book("Книга2", "Автор", 2001, "Жанр", "978-0-0000-0002-2")
        index.add_book(book1)
        index.add_book(book2)
        isbns = list(index)
        assert len(isbns) == 2
    
    def test_multiple_books_same_author(self):
        index = IndexDict()
        book1 = Book("Книга1", "Толстой", 1869, "Роман", "978-0-0000-0001-1")
        book2 = Book("Книга2", "Толстой", 1877, "Роман", "978-0-0000-0002-2")
        index.add_book(book1)
        index.add_book(book2)
        results = index.get_by_author("Толстой")
        assert len(results) == 2
    
    def test_get_by_author_not_found(self):
        index = IndexDict()
        results = index.get_by_author("Несуществующий")
        assert results == []
    
    def test_get_by_year_not_found(self):
        index = IndexDict()
        results = index.get_by_year(9999)
        assert results == []
