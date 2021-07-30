from flask import Flask, render_template, request, redirect, url_for
# import sqlite3
import os
from flask_sqlalchemy import SQLAlchemy

FILE_URI = "sqlite:///new-books-collection.db"

app = Flask(__name__)

all_books = []
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY,
# title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL,
# rating FLOAT NOT NULL)")
# cursor.execute(
#     "INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = FILE_URI
# Optional: But it will silence the deprecation warning in the console.
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified
    # by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create the database file and tables
# This code must come _after_ the class definition
if not os.path.isfile(FILE_URI):
    db.create_all()


# CREATE RECORD
# new_book = Book(id=2, title="G Hotter",
#                 author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        book_name = request.form['BookName']
        book_author = request.form['BookAuthor']
        rating = request.form['Rating']
        new_book = Book(title=book_name, author=book_author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
    # print(all_books)
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route("/add")
def add():
    return render_template('add.html')


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit.html", book=book_selected)


@app.route('/delete')
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run()
