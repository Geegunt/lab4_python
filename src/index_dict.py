from collections.abc import Iterator
from src.book import Book


class IndexDict:
    """
    Словарная коллекция для индексации книг по ISBN, автору и году
    
    Обеспечивает быстрый поиск O(1) по ISBN и O(1) по автору/году
    
    Attributes:
        _isbn_index: Словарь ISBN -> Book
        _author_index: Словарь автор -> список книг
        _year_index: Словарь год -> список книг
    """
    
    def __init__(self) -> None:
        """Инициализация пустых индексов"""
        self._isbn_index: dict[str, Book] = {}
        self._author_index: dict[str, list[Book]] = {}
        self._year_index: dict[int, list[Book]] = {}
    
    def add_book(self, book: Book) -> None:
        """
        Добавление книги во все индексы
        
        Args:
            book: Книга для индексации
        """
        self._isbn_index[book.isbn] = book
        
        if book.author not in self._author_index:
            self._author_index[book.author] = []
        self._author_index[book.author].append(book)
        
        if book.year not in self._year_index:
            self._year_index[book.year] = []
        self._year_index[book.year].append(book)
        
        print(f"[ИНДЕКС] Книга добавлена в индексы: {book.title}")
    
    def remove_book(self, book: Book) -> None:
        """
        Удаление книги из всех индексов
        
        Args:
            book: Книга для удаления из индексов
        """
        if book.isbn in self._isbn_index:
            del self._isbn_index[book.isbn]
        
        if book.author in self._author_index:
            self._author_index[book.author].remove(book)
            if not self._author_index[book.author]:
                del self._author_index[book.author]
        
        if book.year in self._year_index:
            self._year_index[book.year].remove(book)
            if not self._year_index[book.year]:
                del self._year_index[book.year]
        
        print(f"[ИНДЕКС] Книга удалена из индексов: {book.title}")
    
    def __getitem__(self, key: str) -> Book:
        """
        Доступ к книге по ISBN
        
        Args:
            key: ISBN книги
            
        Returns:
            Книга с данным ISBN
            
        Raises:
            KeyError: Если ISBN не найден
        """
        return self._isbn_index[key]
    
    def get_by_author(self, author: str) -> list[Book]:
        """
        Поиск книг по автору
        
        Args:
            author: Имя автора
            
        Returns:
            Список книг автора или пустой список
        """
        return self._author_index.get(author, [])
    
    def get_by_year(self, year: int) -> list[Book]:
        """
        Поиск книг по году издания
        
        Args:
            year: Год издания
            
        Returns:
            Список книг данного года или пустой список
        """
        return self._year_index.get(year, [])
    
    def __len__(self) -> int:
        """
        Количество книг в индексе
        
        Returns:
            Число уникальных ISBN
        """
        return len(self._isbn_index)
    
    def __iter__(self) -> Iterator[str]:
        """
        Итерация по ISBN
        
        Returns:
            Итератор по ISBN
        """
        return iter(self._isbn_index)
    
    def __contains__(self, isbn: str) -> bool:
        """
        Проверка наличия ISBN в индексе
        
        Args:
            isbn: ISBN для проверки
            
        Returns:
            True если ISBN есть в индексе
        """
        return isbn in self._isbn_index
