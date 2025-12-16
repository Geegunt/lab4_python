import random
import json
from pathlib import Path
from src.library import Library
from src.book import Book, RareBook, DigitalBook


_loaded_books: list[Book] = []


def load_books_from_json(filepath: str = None) -> list[Book]:
    """
    Загрузка книг из JSON-файла
    
    Использует кэширование - загружает данные только один раз
    
    Args:
        filepath: Путь к JSON-файлу (по умолчанию books.json)
        
    Returns:
        Список загруженных книг
    """
    global _loaded_books
    if _loaded_books:
        return _loaded_books
    
    if filepath is None:
        filepath = Path(__file__).parent / "books.json"
    
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for item in data["books"]:
        book_type = item.get("type", "book")
        if book_type == "rare":
            book = RareBook(item["title"], item["author"], item["year"],
                           item["genre"], item["isbn"], item["value"])
        elif book_type == "digital":
            book = DigitalBook(item["title"], item["author"], item["year"],
                              item["genre"], item["isbn"], item["file_size_mb"])
        else:
            book = Book(item["title"], item["author"], item["year"],
                       item["genre"], item["isbn"])
        _loaded_books.append(book)
    
    return _loaded_books


def event_add_book(library: Library, step: int) -> None:
    """
    Событие добавления случайной книги в библиотеку
    
    Args:
        library: Библиотека для добавления книги
        step: Номер текущего шага симуляции
    """
    books = load_books_from_json()
    available_books = [b for b in books if b not in library.books]
    if available_books:
        book = random.choice(available_books)
        library + book
        print(f"Шаг {step}: СОБЫТИЕ - Добавлена книга: {book}")
    else:
        print(f"Шаг {step}: СОБЫТИЕ - Все книги уже в библиотеке")


def event_remove_book(library: Library, step: int) -> None:
    """
    Событие удаления случайной книги из библиотеки
    
    Args:
        library: Библиотека для удаления книги
        step: Номер текущего шага симуляции
    """
    if len(library.books) > 0:
        book = library.books[random.randint(0, len(library.books) - 1)]
        library - book
        print(f"Шаг {step}: СОБЫТИЕ - Удалена книга: {book}")
    else:
        print(f"Шаг {step}: СОБЫТИЕ - Невозможно удалить, библиотека пуста")


def event_search_by_author(library: Library, step: int) -> None:
    """
    Событие поиска книг по случайному автору
    
    Args:
        library: Библиотека для поиска
        step: Номер текущего шага симуляции
    """
    books = load_books_from_json()
    authors = list(set(b.author for b in books))
    author = random.choice(authors)
    results = library(author)
    print(f"Шаг {step}: СОБЫТИЕ - Поиск по автору '{author}': найдено {len(results)} книг(и)")
    if results:
        for book in results:
            print(f"  Найдена: {book}")


def event_search_by_genre(library: Library, step: int) -> None:
    """
    Событие поиска книг по случайному жанру
    
    Args:
        library: Библиотека для поиска
        step: Номер текущего шага симуляции
    """
    books = load_books_from_json()
    genres = list(set(b.genre for b in books))
    genre = random.choice(genres)
    results = library(genre, by_genre=True)
    print(f"Шаг {step}: СОБЫТИЕ - Поиск по жанру '{genre}': найдено {len(results)} книг(и)")
    if results:
        for book in results:
            print(f"  Найдена: {book}")


def event_search_by_year(library: Library, step: int) -> None:
    """
    Событие поиска книг по случайному году
    
    Args:
        library: Библиотека для поиска
        step: Номер текущего шага симуляции
    """
    books = load_books_from_json()
    years = list(set(b.year for b in books))
    year = random.choice(years)
    results = library(year)
    print(f"Шаг {step}: СОБЫТИЕ - Поиск по году {year}: найдено {len(results)} книг(и)")
    if results:
        for book in results:
            print(f"  Найдена: {book}")


def event_update_index(library: Library, step: int) -> None:
    """
    Событие проверки консистентности индексов
    
    Args:
        library: Библиотека для проверки
        step: Номер текущего шага симуляции
    """
    print(f"Шаг {step}: СОБЫТИЕ - Проверка индексов")
    print(f"  Книг в коллекции: {len(library.books)}")
    print(f"  Книг в индексе: {len(library.index)}")


def event_search_nonexistent(library: Library, step: int) -> None:
    """
    Событие поиска книги по ISBN
    
    Args:
        library: Библиотека для поиска
        step: Номер текущего шага симуляции
    """
    if len(library.books) > 0:
        existing_book = library.books[random.randint(0, len(library.books) - 1)]
        result = library(existing_book.isbn)
        if result:
            print(f"Шаг {step}: СОБЫТИЕ - Поиск по ISBN '{existing_book.isbn}': Найдена книга: {result}")
    else:
        print(f"Шаг {step}: СОБЫТИЕ - Поиск по ISBN: Нет книги по такому ISBN (библиотека пуста)")


def event_slice_books(library: Library, step: int) -> None:
    """
    Событие получения среза первых книг из коллекции
    
    Args:
        library: Библиотека для получения среза
        step: Номер текущего шага симуляции
    """
    if len(library.books) > 0:
        end = min(3, len(library.books))
        sliced = library.books[0:end]
        print(f"Шаг {step}: СОБЫТИЕ - Получен срез первых {end} книг: извлечено {len(sliced)} книг(и)")
        for book in sliced:
            print(f"  В срезе: {book}")
    else:
        print(f"Шаг {step}: СОБЫТИЕ - Невозможно получить срез, библиотека пуста")


def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    """
    Запуск симуляции работы библиотеки
    
    Args:
        steps: Количество шагов симуляции (по умолчанию 20)
        seed: Seed для генератора случайных чисел (для воспроизводимости)
    """
    if seed is not None:
        random.seed(seed)
    
    library = Library()
    
    events = [
        event_add_book,
        event_remove_book,
        event_search_by_author,
        event_search_by_genre,
        event_search_by_year,
        event_update_index,
        event_search_nonexistent,
        event_slice_books,
    ]

    print("НАЧАЛО СИМУЛЯЦИИ БИБЛИОТЕКИ")
    print(f"Количество шагов: {steps}, Seed: {seed}")
    
    for step in range(1, steps + 1):
        event = random.choice(events)
        event(library, step)
        print()

    print("КОНЕЦ СИМУЛЯЦИИ БИБЛИОТЕКИ")
    print(f"Итоговое состояние библиотеки: {len(library.books)} книг(и)")
