from sqlalchemy import Column, Integer, String

from data.my_db import mydb
from app import db


class User(db.Model):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self):
        super(User, self).__init__()

    def add(self):
        u = User('admin', 'admin@localhost')
        db_session.add(u)

    def __repr__(self):
        return f'<User {self.name!r}>'

if __name__ == '__main__':
    u = User()
    u.add()