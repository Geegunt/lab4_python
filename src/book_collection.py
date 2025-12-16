from src.book import Book


class BookCollection:
    """Коллекция книг с поддержкой стандартных операций Python."""

    def __init__(self) -> None:
        self._books = []
    
    def add_book(self, book: Book) -> None:
        """Добавление книги в коллекцию."""
        self._books.append(book)
    
    def remove_book(self, book: Book) -> None:
        """Удаление книги из коллекции."""
        self._books.remove(book)
    
    def remove_by_index(self, index: int):
        """Удаление книги по индексу."""
        return self._books.pop(index)
    
    def __getitem__(self, index):
        """Доступ к книге по индексу."""
        return self._books[index]
    
    def __iter__(self):
        """Итерация по коллекции."""
        return iter(self._books)
    
    def __len__(self) -> int:
        """Количество книг в коллекции."""
        return len(self._books)
    
    def __contains__(self, book: Book) -> bool:
        """Проверка наличия книги в коллекции."""
        return book in self._books
