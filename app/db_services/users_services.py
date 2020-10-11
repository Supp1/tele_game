from app.models.user import User

from app import db, app


def create_user(chat_id):
    with app.app_context():
        user = User(id=None, chat_id=chat_id)
        db.session.add(user)
        db.session.commit()
    return user


def get_user(chat_id):
    return User.query.filter(User.chat_id == chat_id).first()
