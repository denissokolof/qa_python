from main import BooksCollector
import pytest

class TestBooksCollector:

    # добавление новой книги

    def test_add_new_book_add_two_books(self):
        
        collector = BooksCollector()

        collector.add_new_book('Гордость и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.books_genre) == 2

    def test_add_new_book_add_book_duplicate(self):
        
        collector = BooksCollector()

        collector.add_new_book('Гордость и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('new_book, resalt', [['S' * 42, 0], ['', 0]])
    def test_add_new_book_add_book_with_big_name_and_small_name(self, new_book, resalt):
        
        collector = BooksCollector()

        collector.add_new_book(new_book)

        assert len(collector.books_genre) == resalt


    # устанавливаем книге жанр

    def test_set_book_genre_one_book_with_genre(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
       
        assert collector.books_genre['Гордость и предубеждение и зомби'] == 'Фантастика'


    def test_set_book_genre_with_incorrect_book_with_right_genre(self):

        collector = BooksCollector()

        collector.set_book_genre('Неизвестная книга', 'Фантастика')

        assert len(collector.books_genre) == 0

    def test_set_book_genre_with_correct_book_with_incorrect_genre(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Роман')

        assert collector.books_genre['Гордость и предубеждение и зомби'] == ''

    # получаем жанр книги по её имени   

    def test_get_book_genre_with_correct_book_and_correct_genre(self):

        collector = BooksCollector()

        collector.books_genre = {'Гордость и предубеждение и зомби': 'Фантастика'}

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    # выводим список книг с определённым жанром

    def test_get_book_get_books_with_specific_genre(self):

        collector = BooksCollector()

        collector.books_genre = {'Гордость и предубеждение и зомби': 'Фантастика', 'Зомби дома': 'Фантастика', 'Котенок Гаф' : 'Мультфильмы'}

        book_specific_genre = collector.get_books_with_specific_genre('Мультфильмы')

        assert 'Котенок Гаф' in book_specific_genre and (len(book_specific_genre) == 1)

    # получаем словарь books_genre

    def test_get_books_genre_with_three_books_and_three_genre(self):
            
        collector = BooksCollector()

        collector.books_genre = {'Гордость и предубеждение и зомби': 'Фантастика', 'Зомби дома': 'Фантастика', 'Котенок Гаф' : 'Мультфильмы'}

        assert len(collector.get_books_genre()) == 3

    # возвращаем книги, подходящие детям

    def test_get_books_for_children_with_one_book_for_children(self):
            
        collector = BooksCollector()

        collector.books_genre = {'Гордость и предубеждение и зомби': 'Детективы', 'Зомби дома': 'Ужасы', 'Котенок Гаф' : 'Мультфильмы'}

        book__for_children = collector.get_books_for_children()

        assert len(book__for_children) == 1 and 'Котенок Гаф' in book__for_children

    # добавляем книгу в Избранное

    def test_add_book_in_favorites_one_book(self):

        collector = BooksCollector()

        collector.books_genre = {'Гордость и предубеждение и зомби': 'Детективы', 'Зомби дома': 'Ужасы', 'Котенок Гаф' : 'Мультфильмы'}

        collector.add_book_in_favorites('Зомби дома') 
        
        assert 'Зомби дома' in collector.favorites



    # удаляем книгу из Избранного

    def test_delete_book_from_favorites_one_book(self):

        collector = BooksCollector()

        collector.favorites = ['Котенок Гаф']

        collector.delete_book_from_favorites('Котенок Гаф')

        assert  len(collector.favorites) == 0


    # получаем список Избранных книг
    
    def test_get_list_of_favorites_books_with_two_books(self):

        collector = BooksCollector()

        collector.favorites = ['Котенок Гаф', 'Зомби дома']

        assert len(collector.get_list_of_favorites_books()) == 2
