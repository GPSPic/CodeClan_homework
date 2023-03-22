DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    author_id INT NOT NULL REFERENCES authors(id) ON DELETE CASCADE
);

INSERT INTO authors (name) VALUES ('Stephen King');
INSERT INTO authors (name) VALUES ('Agatha Christie');
INSERT INTO authors (name) VALUES ('J.R.R. Tolkien');

INSERT INTO books (title, genre, author_id) VALUES ('IT', 'Horror', 1);
INSERT INTO books (title, genre, author_id) VALUES ('Hercules Poirot', 'Mystery', 2);
INSERT INTO books (title, genre, author_id) VALUES ('The Hobbit', 'Fantasy', 3);

