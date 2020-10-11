import random

from app.models.user import User
from app.models.quest_models import Persona

from app import db


def create_user(chat_id) -> User:
    try:
        a = random.randint(1, 10) * 20
        b = random.randint(10, 120)
        c = random.randint(1, 10)

        persona = Persona(strength=a, intelligence=b, agility=c)
        db.session.add(persona)
        db.session.flush()

        user = User(id=None, chat_id=chat_id, persona_id=persona.id)
        db.session.add(user)
        db.session.commit()
        return user
    except Exception:
        db.session.rollback()
        raise


def get_user(chat_id) -> User:
    return User.query.filter(User.chat_id == chat_id).first()
