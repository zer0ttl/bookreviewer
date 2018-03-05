from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(128), index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(256))
    reviews = db.relationship("Review", backref="user", lazy=True)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    modified_at = db.Column(db.DateTime(),
                            server_default=db.func.now(),
                            server_onupdate=db.func.now())

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(64), unique=True)
    title = db.Column(db.String(256))
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    year_published_id = db.Column(db.Integer,
                               db.ForeignKey("year.id"),
                               nullable=False)
    modified_at = db.Column(db.DateTime(),
                            server_default=db.func.now(),
                            server_onupdate=db.func.now())

    def __repr__(self):
        return '<Book {}>'.format(self.title)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    books = db.relationship("Book", backref="author", lazy=True)

    def __repr__(self):
        return '<Author> {}>'.format(self.name)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.Text)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    modified_at = db.Column(db.DateTime(),
                            server_default=db.func.now(),
                            server_onupdate=db.func.now())


class Year(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, unique=True)