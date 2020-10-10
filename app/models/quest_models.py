from app import db


class BotMessage(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    message = db.Column(db.String(2048), nullable=False)


class Action(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    user_phrase = db.Column(db.String(2048), nullable=False)
    bot_message = db.relation('bot_message', lazy=True)


class UserDecision(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    action = db.relation('action_id', lazy=True)
    state = db.relation('state_id', lazy=True)
