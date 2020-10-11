from app.models.quest_models import BotMessage


def get_first_message():
    return BotMessage.query.first()
