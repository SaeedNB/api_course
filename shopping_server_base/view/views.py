import json

from flask import request

from app import app
from dao.items import ItemDao
from dao.users import UserDao

user_dao = UserDao()
item_dao = ItemDao()


@app.route('/users', methods=["GET"])
def get_users():
    users = user_dao.get_all_user()
    user_list = []
    for user in users:
        user_list.append(
            {
                "name": user.name,
                "username": user.username,
                "email": user.email
            }

        )
    return json.dumps(user_list)


@app.route('/users/<user_id>', methods=["GET"])
def get_user_by_id(user_id):
    user = user_dao.get_user_by_id(user_id)
    if user:
        my_user = {
            "name": user.name,
            "username": user.username,
            "email": user.email
        }
        return json.dumps(my_user)
    return "User not exists"


@app.route('/users', methods=["POST"])
def insert_user():
    data = json.loads(request.data)
    name = data.get("name")
    password = data.get("password")
    username = data.get("username")
    email = data.get("email")
    user_dao.create_user(name=name, password=password, username=username, email=email)
    return "one user insert"


@app.route('/login', methods=["POST"])
def login():
    data = json.loads(request.data)
    username = data.get("username")
    password = data.get("password")
    res = user_dao.login(username, password)
    my_dict = {
        "status": res
    }
    return json.dumps(my_dict)


@app.route('/users/<user_id>', methods=["PUT"])
def update_user(user_id):
    data = json.loads(request.data)
    name = data.get("name")
    password = data.get("password")
    username = data.get("username")
    email = data.get("email")
    user_dao.update_user(user_id=user_id, name=name, password=password, email=email, username=username)
    return "update user"


@app.route('/users/<user_id>', methods=["DELETE"])
def delete_user(user_id):
    user_dao.delete_user(user_id)
    return "delete user"


@app.route('/items', methods=["GET"])
def get_items():
    items = item_dao.get_all()
    my_list = []
    for item in items:
        my_list.append({
            "name": item.name,
            "category": item.category
        })
    return json.dumps(my_list)


@app.route('/item_by_category/<category>', methods=["GET"])
def get_items_by_category(category):
    items = item_dao.get_item_by_category(category=category)
    my_list = []
    for item in items:
        my_list.append({
            "name": item.name,
            "category": item.category
        })
    return json.dumps(my_list)


@app.route('/items', methods=["POST"])
def insert_item():
    data = json.loads(request.data)
    name = data.get("name")
    category = data.get("category")
    item_dao.create_item(name=name, category=category)
    return "insert item"


@app.route('/items/<item_id>', methods=["PUT"])
def update_item(item_id):
    return "update item"


@app.route('/items/<item_id>', methods=["DELETE"])
def delete_item(item_id):
    return "delete item"


@app.route('/shopping_cart', methods=["GET"])
def get_carts():
    return "get carts"


@app.route('/shopping_cart', methods=["POST"])
def insert_cart():
    return "insert cart"


@app.route('/shopping_cart/<cart_id>', methods=["PUT"])
def update_cart(cart_id):
    return "cart id"


@app.route('/shopping_cart', methods=["DELETE"])
def delete_post():
    return "delete cart"
