from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.BigInteger)
    state_id = db.Column(db.BigInteger, db.ForeignKey('bot_message.id'), nullable=False, default=1)
