from app import db


class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    chat_id = db.Column(db.BigInteger)
    state = db.relationship('action', lazy=True)
