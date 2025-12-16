from src.book import Book
from src.book_collection import BookCollection
from src.index_dict import IndexDict


class Library:
    """
    Класс библиотеки с магическими методами для управления книгами
    
    Использует магические методы __add__, __sub__, __call__ для
    добавления, удаления и поиска книг соответственно
    
    Attributes:
        books: Коллекция книг (BookCollection)
        index: Индекс для быстрого поиска (IndexDict)
    """
    
    def __init__(self) -> None:
        """Инициализация пустой библиотеки"""
        self.books = BookCollection()
        self.index = IndexDict()
    
    def __add__(self, book: Book) -> "Library":
        """
        Добавление книги через оператор +
        
        Args:
            book: Книга для добавления
            
        Returns:
            Ссылка на библиотеку для цепочки операций
        """
        self.books.add_book(book)
        self.index.add_book(book)
        print(f"[БИБЛИОТЕКА] Добавлена: {book}")
        return self
    
    def __sub__(self, book: Book) -> "Library":
        """
        Удаление книги через оператор -
        
        Args:
            book: Книга для удаления
            
        Returns:
            Ссылка на библиотеку для цепочки операций
            
        Raises:
            ValueError: Если книга не найдена
        """
        self.books.remove_book(book)
        self.index.remove_book(book)
        print(f"[БИБЛИОТЕКА] Удалена: {book}")
        return self
    
    def __call__(self, query: str | int, by_genre: bool = False) -> Book | list[Book] | None:
        """
        Универсальный поиск по автору, году, ISBN или жанру
        
        Args:
            query: Поисковый запрос (int - год, str - автор/ISBN/жанр)
            by_genre: Если True, поиск по жанру
            
        Returns:
            Книга по ISBN, список книг по автору/году/жанру, или None
        """
        if isinstance(query, int):
            return self.index.get_by_year(query)
        elif isinstance(query, str):
            if query.startswith("978"):
                try:
                    return self.index[query]
                except KeyError:
                    return None
            if by_genre:
                return [book for book in self.books if book.genre == query]
            return self.index.get_by_author(query)
        return None
