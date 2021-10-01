from sqlalchemy import Column, Integer, String

from data.my_db import Base, db_session


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        super().__init__()
        self.name = name
        self.email = email

    def add(self):
        u = User('admin', 'admin@localhost')
        db_session.add(u)

    def __repr__(self):
        return f'<User {self.name!r}>'