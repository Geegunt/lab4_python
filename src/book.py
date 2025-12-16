class Book:
    """Базовый класс книги с основными атрибутами."""
    
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
    
    def __repr__(self) -> str:
        return f"Книга('{self.title}', автор: {self.author}, {self.year} г.)"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return False
        return self.isbn == other.isbn


class RareBook(Book):
    """Редкая книга с указанием стоимости."""
    
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, value: float):
        super().__init__(title, author, year, genre, isbn)
        self.value = value
    
    def __repr__(self) -> str:
        return f"Редкая книга('{self.title}', автор: {self.author}, {self.year} г., {self.value}₽)"


class DigitalBook(Book):
    """Электронная книга с указанием размера файла."""
    
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, file_size_mb: float):
        super().__init__(title, author, year, genre, isbn)
        self.file_size_mb = file_size_mb
    
    def __repr__(self) -> str:
        return f"Электронная книга('{self.title}', автор: {self.author}, {self.year} г., {self.file_size_mb} МБ)"