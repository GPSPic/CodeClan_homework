from flask import render_template, request, redirect
from app import app
from models.library import library, add_book, remove_book
from models.book import Book

@app.route('/')
def index():
    return render_template('index.html', title="Home")