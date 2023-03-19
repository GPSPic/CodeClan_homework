from models.book import Book

book1 = Book("Automate the Boring Stuff with Python", "Al Sweigart", "Psychological horror")
book2 = Book("The Wandering Inn", "pirateaba", "Fantasy")
book3 = Book("Le Misanthrope", "Moliere", "Comedy")
book4 = Book("Do androids dream of electric sheep?", "Philip K. Dick", "Science-Fiction")
book5 = Book("And then there were none", "Agatha Christie", "Mystery")
book_list = [book1, book2, book3]

def add_book(book):
    if book not in book_list:
        book_list.append(book)

def delete_book(book):
    if book in book_list:
        book_list.remove(book)

def check_book_out(book):
    if book.available:
        book.available = False

def check_book_in(book):
    if not book.available:
        book.available = True


























# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.book_list = []

#     def add_book(self, book):
#         if book not in self.book_list:
#             self.book_list.append(book)

#     def remove_book(self, book):
#         if book in self.book_list:
#             self.book_list.remove(book)

#     def list_all_books(self):
#         all_books = [book for book in self.book_list]
#         return all_books       

#     def list_all_books_titles(self):
#         all_books_titles = [book.title for book in self.book_list]
#         return all_books_titles   

