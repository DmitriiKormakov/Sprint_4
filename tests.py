import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_same_book_three_times_book_added_once(self, collector):
        collector.add_new_book("Сияние")
        collector.add_new_book("Сияние")
        collector.add_new_book("Сияние")
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize("valid_books", ["A", "A" * 40])
    def test_add_new_book_add_border_book_name(self, valid_books):
        collector = BooksCollector()
        collector.add_new_book(valid_books)
        assert valid_books in collector.get_books_genre()
        assert collector.get_books_genre()[valid_books] == ""

    def test_set_book_genre_set_valid_genre_for_existing_book(self, collector):
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        assert collector.get_book_genre("Мастер и Маргарита") == "Фантастика"

    def test_set_book_genre_cannot_set_genre_for_nonexistent_book(self, collector):
        collector.set_book_genre("Несуществующая книга", "Фантастика")
        assert collector.get_book_genre("Несуществующая книга") is None

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book("Звёздные войны")
        collector.add_new_book("Оно")
        collector.set_book_genre("Звёздные войны", "Фантастика")
        collector.set_book_genre("Оно", "Ужасы")

        fantasy_books = collector.get_books_with_specific_genre("Фантастика")
        assert len(fantasy_books) == 1
        assert "Звёздные войны" in fantasy_books

    def test_get_books_for_children_returns_only_child_friendly_books(self):
        collector = BooksCollector()
        collector.add_new_book("Король Лев")
        collector.add_new_book("Оно")
        collector.set_book_genre("Король Лев", "Мультфильмы")
        collector.set_book_genre("Оно", "Ужасы")

        children_books = collector.get_books_for_children()
        assert "Король Лев" in children_books
        assert "Оно" not in children_books

    def test_add_book_in_favorites_add_existing_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Сомнительная правда")
        collector.add_book_in_favorites("Сомнительная правда")
        assert "Сомнительная правда" in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_remove_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.add_book_in_favorites("Оно")
        collector.delete_book_from_favorites("Оно")
        assert "Оно" not in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 0

    @pytest.mark.parametrize(
        "expected_favorites",
        [
            [
                "Звёздные войны",
                "Сияние",
                "Шерлок Холмс",
                "Король Лев",
                "Сомнительная правда",
                "Оно",
            ]
        ],
    )
    def test_get_list_of_favorites_books_shows_list_of_favorite_books(
        self, collector_with_favorites, expected_favorites
    ):
        favorites = collector_with_favorites.get_list_of_favorites_books()

        assert len(favorites) == len(expected_favorites)
        assert set(favorites) == set(expected_favorites)
        for book in expected_favorites:
            assert book in favorites
