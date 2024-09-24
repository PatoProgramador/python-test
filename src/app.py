from flask import Flask, jsonify, request
from flask_cors import CORS

from src.config import appConfig
from src.routes.BookRoute import mainBook

app = Flask(__name__)

# CORS config

CORS(app, resources={r"/*": {"origins": "*"}})

# Config dev
app.config.from_object(appConfig['development'])
# Config para produccion
# app.config.from_object(appConfig['production'])

def page_not_found(error):
    return jsonify({"message": "Not found"}), 404

app.register_blueprint(mainBook, url_prefix='/api/books')

# Error handlers
app.register_error_handler(404, page_not_found)

if __name__ == '__main__':
    app.run()
