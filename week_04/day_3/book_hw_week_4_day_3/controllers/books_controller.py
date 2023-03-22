from flask import Flask, render_template, request, redirect
from repositories import book_repository
from repositories import author_repository
from models.author import Author
from models.book import Book

from flask import Blueprint

books_blueprint = Blueprint("book", __name__)

# why you no work with '/books'?
@books_blueprint.route('/books/')
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books=books)

@books_blueprint.route('/books/<id>')
def show_one_book(id):
    selected_book = book_repository.select(id)
    return render_template('/books/show.html', book=selected_book)

@books_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete(id):
    book_repository.delete(id)
    return redirect('/books/')

@books_blueprint.route('/books/new')
def add_new_page():
    # authors = author_repository.select_all() not needed in this case
    return render_template('/books/new.html')

@books_blueprint.route('/books/', methods=['POST'])
def add_new_book():
    title = request.form['title']
    genre = request.form['genre']
    author = Author(request.form['author'])
    author_repository.save(author)
    book = Book(title, genre, author)
    book_repository.save(book)
    return redirect('/books/')
