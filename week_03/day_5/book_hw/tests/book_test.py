import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        book1 = Book("Automate the Boring Stuff with Python", "Al Sweigart", "Psychological horror")
        book2 = Book("The Wandering Inn", "pirateaba", "Fantasy")
        book3 = Book("Le Misanthrope", "Moliere", "Comedy")
