from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping_server.sqlite'
db = SQLAlchemy(app)
db.create_all()

from view.views import *

if __name__ == '__main__':
    app.run()
