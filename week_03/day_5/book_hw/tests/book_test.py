import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("Automate the Boring Stuff with Python", "Al Sweigart", "Psychological horror")
        self.book2 = Book("The Wandering Inn", "pirateaba", "Fantasy")
        self.book3 = Book("Le Misanthrope", "Moliere", "Comedy")

# test 1 - book has title
    def test_book_has_title(self):
        self.assertEqual("Le Misanthrope", self.book3.title)

# test 2 - book has author
    def test_book_has_author(self):
        self.assertEqual("Moliere", self.book3.author)
                         
# test 3 - book has genre
    def test_book_has_genre(self):
        self.assertEqual("Psychological horror", self.book1.genre)