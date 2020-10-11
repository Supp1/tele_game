from app import db
from app.models.user import User


def create_user(chat_id):
    user = User()