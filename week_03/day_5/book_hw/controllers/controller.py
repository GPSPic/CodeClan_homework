from flask import render_template, request, redirect

from app import app
from models.library import book_list, add_book, delete_book, check_book_out, check_book_in
from models.book import Book

@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/books/')
def books():
    return render_template('books/index.html', title="Books", books=book_list)

@app.route('/books/<id>')
def single_book(id):
    return render_template('books/show.html', title="Collection", book=book_list[int(id)], id=id)
# , library=book_list

@app.route('/addnew')
def add_book_page():
    return render_template('addnew.html', title="Add New")

@app.route('/addnew', methods=['POST'])
def add_book_to_library():
    title = request.form['title']
    author = request.form['Rubber duck']
    genre = request.form['genre']
    new_book = Book(title, author, genre)
    add_book(new_book)
    return redirect('/books')

@app.route('/books/<id>/delete', methods=['POST'])
def remove_book_from_library(id):
    book = book_list[int(id)]
    delete_book(book)
    return redirect('/books')

# @app.route('/books/<id>/availability', methods=['POST'])
# def update_available(id):
#     book = book_list[int(id)]
#     current_availability = request.form('availability')
#     if current_availability == 'check-in':
#         check_book_in(book)
#     else:
#         check_book_out(book)
#     return redirect('/books/<id>')


# works by defining the id in python/flask in the show.html page {{id}} and from the GET route for /books/id (show.html)
# @app.route('/books/<id>/delete', methods=['POST'])
# def remove_book_from_library(id):
#     book = book_list[int(id)]
#     delete_book(book)
#     return redirect('/books')

# @app.route('/books/<id>/checkout', methods=['POST'])
# def check_book_out_of_library(id):
#     book = book_list[int(id)]
#     check_book_out(book)
#     return redirect('/books/<id>')