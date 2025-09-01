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
    def test_add_new_book_add_same_book_three_times_book_added_once(self):
        collector = BooksCollector()
        collector.add_new_book("Сияние")
        collector.add_new_book("Сияние")
        collector.add_new_book("Сияние")
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize("book_name", ["A", "A" * 40])
    def test_add_new_book_add_border_book_name(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()
        assert collector.get_books_genre()[book_name] == ""

    def test_set_book_genre_set_valid_genre_for_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        assert collector.get_book_genre("Мастер и Маргарита") == "Фантастика"

    def test_set_book_genre_cannot_set_genre_for_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre("Несуществующая книга", "Фантастика")
        assert collector.get_book_genre("Несуществующая книга") is None

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.books_genre = {
            "Звёздные войны": "Фантастика",
            "Оно": "Ужасы",
            "Сияние": "Ужасы",
        }
        horror_books = collector.get_books_with_specific_genre("Ужасы")
        assert horror_books == ["Оно", "Сияние"]

    def test_get_books_for_children_returns_only_child_friendly_books(self):
        collector = BooksCollector()
        collector.books_genre = {
            "Король Лев": "Мультфильмы",
            "Оно": "Ужасы",
            "Шерлок Холмс": "Детективы",
            "Сомнительная правда": "Комедии",
        }

        children_books = collector.get_books_for_children()
        assert "Король Лев" in children_books
        assert "Оно" not in children_books

    def test_add_book_in_favorites_add_existing_book_to_favorites(self):
        collector = BooksCollector()
        collector.books_genre = {"Сомнительная правда": "Комедии"}
        collector.add_book_in_favorites("Сомнительная правда")
        assert "Сомнительная правда" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_remove_book_from_favorites(self):
        collector = BooksCollector()
        collector.favorites = ["Оно"]
        collector.delete_book_from_favorites("Оно")
        assert "Оно" not in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_returns_favorites(self):
        collector = BooksCollector()
        expected_favorites = ["Book1", "Book2", "Book3"]
        collector.favorites = expected_favorites
        assert collector.get_list_of_favorites_books() == expected_favorites

    def test_get_book_genre_returns_correct_genre_for_existing_book(self):
        collector = BooksCollector()
        collector.books_genre = {"Сияние": "Ужасы"}
        assert collector.get_book_genre("Сияние") == "Ужасы"
        
    def test_get_books_genre_returns_full_dict(self):
        collector = BooksCollector()
        expected_dict = {"Звёздные войны": "Фантастика", "Оно": "Ужасы"}
        collector.books_genre = expected_dict
        assert collector.get_books_genre() == expected_dict
