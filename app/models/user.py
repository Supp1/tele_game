from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, nullable=False, unique=True)
    state_id = db.Column(db.Integer, db.ForeignKey('bot_message.id'), nullable=False, default=1)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)
