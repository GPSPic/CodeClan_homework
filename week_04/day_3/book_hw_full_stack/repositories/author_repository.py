from db.run_sql import run_sql

from models.author import Author
from models.book import Book

def save(author):
    sql = "INSERT INTO authors (name) VALUES (%s) RETURNING *"
    values = [author.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def select_all():
    authors= []
    sql = "SELECT * FROM authors"
    results= run_sql(sql)
    for row in results:
        author= Author(row['name'], row['id'])
        authors.append(author)
    return authors

def select(id):
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        author = Author(result['name'], result['id'])
    return author

