from sqlalchemy.orm import sessionmaker
from .entities.Book import Book, engine

class BookManager:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add_book(self, title, author, year):
        new_book = Book(title=title, author=author, year=year)
        self.session.add(new_book)
        self.session.commit()

    def get_all_books(self):
        return self.session.query(Book).all()

    def find_book(self, query):
        return self.session.query(Book).filter(
            (Book.title.contains(query)) | (Book.author.contains(query))
        ).all()

    def delete_book(self, book_id):
        book = self.session.query(Book).get(book_id)
        if book:
            self.session.delete(book)
            self.session.commit()
        else:
            raise ValueError(f"Book with id {book_id} does not exist")
