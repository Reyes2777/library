from books import Book

class Book_store(object):

    def __init__(self):
        self.library = []
        self.create_id = 1

    def add_book(self):
        book = Book()
        book.create_book(self.create_id)
        self.create_id += 1
        self.library.append(book)

    def show_books(self, params):
        for book in self.library:
            print(book[params])

    def del_book(self):
        book = 
