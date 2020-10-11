from app import db


class BotMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(2048), nullable=False)
    actions = db.relationship('Action', backref='bot_message', lazy=True)


class Action(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_phrase = db.Column(db.String(2048), nullable=False)
    bot_message_id = db.Column(db.BigInteger, db.ForeignKey('bot_message.id'), nullable=False)


class UserDecision(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action_id = db.Column(db.BigInteger, db.ForeignKey('action.id'), nullable=False)
    state_id = db.Column(db.BigInteger, db.ForeignKey('bot_message.id'), nullable=False)
