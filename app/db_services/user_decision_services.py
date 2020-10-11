from app.models.quest_models import BotMessage, UserDecision


def find_by_action_id(action_id):
    return UserDecision.query.filter(UserDecision.action_id == action_id).first()
