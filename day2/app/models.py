from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(256), nullable=False)

    def __init__(self, name, email, address, password):
        self.name = name
        self.email = email
        self.address = address
        self.password = generate_password_hash(password)


class Book(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(150))
    
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address
