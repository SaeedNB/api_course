import bcrypt

from app import db
from model.users import Users


class UserDao:
    def __init__(self):
        self.user_model = Users()
        pass

    def create_user(self, name, username, password, email):
        hashed_pass = self.get_hashed_password(password.encode("utf8"))
        new_user = Users(name=name, username=username, password=hashed_pass, email=email)
        db.session.add(new_user)
        db.session.commit()

    def login(self, username, password):
        user = Users.query.filter(Users.username == username).first()
        if user:
            hashed_password = user.password
            res = self.check_password(password.encode("utf8"), hashed_password)
            return res

        return False

    def get_user_by_id(self, user_id):
        return Users.query.get(user_id)

    def get_all_user(self):
        return Users.query.all()

    def update_user(self, user_id, name, username, password, email):
        user = Users.query.get(user_id)
        user.name = name
        user.username = username
        user.password = password
        user.email = email
        db.session.commit()

    def delete_user(self, user_id):
        user = Users.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()

    def get_hashed_password(self, plain_text_password):
        return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

    def check_password(self, plain_text_password, hashed_password):
        return bcrypt.checkpw(plain_text_password, hashed_password)
