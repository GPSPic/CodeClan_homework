import unittest
from models.book import Book
from models.library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("Automate the Boring Stuff with Python", "Al Sweigart", "Psychological horror")
        self.book2 = Book("The Wandering Inn", "pirateaba", "Fantasy")
        self.book3 = Book("Le Misanthrope", "Moliere", "Comedy")
        self.book4 = Book("Do androids dream of electric sheep?", "Philip K. Dick", "Science-Fiction")
        self.book5 = Book("And then there were none", "Agatha Christie", "Mystery")
        self.book_list = [self.book1, self.book2, self.book3]
        self.library = Library("Read a Book, People! Library")
        

# test 4 - Library can add books and can only add them once
    def test_library_can_add_books(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book1)
        self.assertEqual(1, len(self.library.book_list))

# test 5 - Library can remove books and cannot remove non-existing books
    def test_library_can_remove_books(self):
        self.library.add_book(self.book1)
        self.library.remove_book(self.book2)
        self.assertEqual(1, len(self.library.book_list))
        self.library.remove_book(self.book1)
        self.assertEqual(0, len(self.library.book_list))

# test 6 - list all books available in library
    def test_list_all_books_in_library(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)
        expected = [self.book1, self.book2, self.book3]
        function_return = self.library.list_all_books()
        self.assertEqual(expected, function_return)

# test 7 - list all book titles for books available
    def test_list_all_book_titles_in_library(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)
        expected = [
            "Automate the Boring Stuff with Python",
            "The Wandering Inn",
            "Le Misanthrope",
            ]
        function_return = self.library.list_all_books_titles()
        self.assertEqual(expected, function_return)

# test 8 - find book by title
    # def test_find_book_by_title(self):


# test 9 - find book by author

# test 10 - find book by genre