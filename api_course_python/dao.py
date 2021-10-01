from data.book import Book


class Bookdao:

    def get(self):
        book = Book.query.all()
        print(book.name)
