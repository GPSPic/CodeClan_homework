from models.author import Author
from models.book import Book

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author1 = Author("Ernest Hemmingway")
author_repository.save(author1)

book1 = Book("The Old and the Sea", "Fiction", author1)
book_repository.save(book1)
