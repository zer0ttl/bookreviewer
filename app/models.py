from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(128), index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(256))
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    modified_at = db.Column(db.DateTime(),
                            server_default=db.func.now(),
                            server_onupdate=db.func.now())

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(64), unique=True)
    title = db.Column(db.String(256))
    author = db.Column(db.String(256))
    year_published = db.Column(db.String(16))
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    modified_at = db.Column(db.DateTime(),
                            server_default=db.func.now(),
                            server_onupdate=db.func.now())

    def __repr__(self):
        return '<Book {}>'.format(self.title)
