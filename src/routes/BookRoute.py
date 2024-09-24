from crypt import methods

from flask import Blueprint, jsonify, request

# Entities
from ..models.entities import Book

# Models
from ..models.BookModel import BookModel
from ..models.validations.BookValidations import validate_request

mainBook = Blueprint('book_blueprint', __name__)
bookModel = BookModel()

@mainBook.route('/', methods=['GET'])
def get_all_books():
    try:
        books : [Book] = bookModel.get_all_books()

        if len(books) == 0:
            return jsonify({"message": "There are no books in the database :( try creating one"}), 400
        else:
            return jsonify([book.to_json() for book in books]), 200

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@mainBook.route('/search', methods=['GET'])
def search_books():
    print("Search books route reached")  # Añadir esto para depuración
    query = request.args.get('query', '')
    print(f"Query received: {query}")
    try:
        found_books = bookModel.find_book(query)

        if not found_books:
            return jsonify({"message": "No books found matching the query."}), 404

        return jsonify([book.to_json() for book in found_books]), 200

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

@mainBook.route('/', methods=['POST'])
def create_book():
    try:
        data = request.get_json()
        validate_request(data)

        title = data.get('title')
        author = data.get('author')
        year = data.get('year')

        new_book = bookModel.add_book(title, author, year)

        return jsonify(new_book.to_json()), 201

    except ValueError as ex:
        return jsonify({"message": str(ex)}), 400

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

@mainBook.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    try:
        bookModel.delete_book(book_id)
        return jsonify({"message": "Book deleted successfully"}), 204

    except ValueError as ve:
        return jsonify({"message": str(ve)}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
