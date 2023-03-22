from flask import Flask, render_template, request, redirect
# from repositories import book_repository
from repositories import author_repository
from models.author import Author

from flask import Blueprint

authors_blueprint = Blueprint("authors", __name__)

@authors_blueprint.route("/authors")
def authors():
    authors = author_repository.select_all()
    return render_template("/authors/index.html", all_authors=authors)
