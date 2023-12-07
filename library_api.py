from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#database link would be here
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql12668160:YUdpy75Q41@sql12.freemysqlhosting.net/sql12668160'
db = SQLAlchemy(app)

#making book class for table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

#creating the table
with app.app_context():
    db.create_all()

# Endpoint to retrieve all books
@app.route('/api/books', methods=['GET'])
def get_all_books():
    try:
        books = Book.query.all()
        books_list = [{'id': book.id, 'title': book.title, 'author': book.author} for book in books]
        return jsonify({'books': books_list})
    except Exception as e:
        return jsonify({'error': str(e)}), 500




# Endpoint to add a new book
@app.route('/api/books', methods=['POST'])
def add_new_book():
    try:
        data = request.get_json()
        new_book = Book(title=data['title'], author=data['author'])


        existing_book = Book.query.filter_by(title=new_book.title, author=new_book.author).first()
        if existing_book:
            return jsonify({'error': 'Book already exists'}), 400

        db.session.add(new_book)
        db.session.commit()
        return jsonify({'message': 'Book added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500



# Endpoint to update book details
@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    try:
        book = Book.query.get(book_id)
        if not book:
            return jsonify({'error': 'Book not found'}), 404
        
        data = request.get_json()

        # Update only the provided fields
        if 'title' in data:
            book.title = data['title']
        if 'author' in data:
            book.author = data['author']
        
        db.session.commit()
        return jsonify({'message': 'Book updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
