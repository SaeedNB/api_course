from model.items import Items
from app import db


class ItemDao:

    def create_item(self, name, category):
        item = Items(name=name, category=category)
        db.session.add(item)
        db.session.commit()

    def get_item_by_category(self, category):
        items = Items.query.filter(Items.category == category).all()
        return items

    def get_all(self):
        items = Items.query.all()
        return items