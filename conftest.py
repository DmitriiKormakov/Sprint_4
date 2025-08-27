import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def collector_with_books_and_genres(collector):
    books = {
        "Звёздные войны": "Фантастика",
        "Сияние": "Ужасы",
        "Шерлок Холмс": "Детективы",
        "Король Лев": "Мультфильмы",
        "Сомнительная правда": "Комедии",
        "Оно": "Ужасы",
    }

    for book, genre in books.items():
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

    return collector


@pytest.fixture
def collector_with_favorites(collector_with_books_and_genres):
    for book in collector_with_books_and_genres.books_genre.keys():
        collector_with_books_and_genres.add_book_in_favorites(book)
    return collector_with_books_and_genres
