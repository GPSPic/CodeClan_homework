import unittest
from models.book import Book
from models.library import Library

class TestLibrary(unittest.TestCase):
    def setUp():
        book1 = Book("Automate the Boring Stuff with Python", "Al Sweigart", "Psychological horror")
        book2 = Book("The Wandering Inn", "pirateaba", "Fantasy")
        book3 = Book("Le Misanthrope", "Moliere", "Comedy")
        library = [book1, book2, book3]

