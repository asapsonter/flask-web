from flask_login import UserMixin
from init import db


class User(UserMixin, db.Model):
    id = db.column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __repr__(self):
        return'<User %r>' % self.id

    def __init__(self, email, password, name):
        db.create_all()
        self.email = email
        self.password = password
        self.name = name
