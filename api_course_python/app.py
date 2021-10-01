import json
import time
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from dao import Bookdao

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_app.sqlite'
db = SQLAlchemy(app)

@app.route("/books", methods=["GET"])
def get_all():
    book_dao = Bookdao()
    book_dao.get()


@app.route("/books", methods=["GET"])
def get_all():
    time.sleep(2)
    res = []

    book_list = Book.query.all()
    for book in book_list:
        res.append({"id": book.id, "name": book.name, "author_name": book.author_name})
    return json.dumps(res)


@app.route("/books", methods=["POST"])
def create():
    data = json.loads(request.data)
    name = data.get("name")
    author_name = data.get("author_name")
    book = Book(name=name, author_name=author_name)
    db.session.add(book)
    db.session.commit()
    return "successfully inserted"


@app.route("/books/<book_id>", methods=["PUT"])
def update(book_id):
    book = Book.query.get(book_id)
    data = json.loads(request.data)
    name = data.get("name")
    author_name = data.get("author_name")
    book.name = name
    book.author_name = author_name
    db.session.commit()
    return "successfully updated"


@app.route("/books/<book_id>", methods=["DELETE"])
def delete(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return "successfully deleted"


if __name__ == '__main__':
    app.run()
