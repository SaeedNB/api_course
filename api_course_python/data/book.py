from flask_sqlalchemy import SQLAlchemy

from app import app

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    author_name = db.Column(db.String(80), unique=True, nullable=False)
