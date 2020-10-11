from app.models.quest_models import Action


def get_actions_by_message_id_and_phrase(bot_message_id, phrase):
    return Action.query\
        .filter(Action.bot_message_id == bot_message_id) \
        .filter(Action.user_phrase.contains(phrase))\
        .all()