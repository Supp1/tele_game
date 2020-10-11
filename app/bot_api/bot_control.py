import random
import re

from telebot import types

from app import bot
from app.db_services import users_services, action_services, user_decision_services
from app.models.quest_models import *
from app.models.user import *


def trigger_controls(updates):
    update = types.Update.de_json(updates)
    bot.process_new_updates([update])


@bot.message_handler(commands=["start"])
def send_welcome(message):
    user = users_services.get_user(message.chat.id)
    if user is not None:
        user.state_id = 1
        db.session.commit()
    else:
        users_services.create_user(message.chat.id)
    bot.send_animation(message.chat.id, "https://gph.is/g/ZdX9B61")
    bot.send_message(message.chat.id, "Hi, i am Highlighter bot.")
    startBotMessage: BotMessage = BotMessage.query.first()
    keyboard = generate_user_action(startBotMessage)
    bot.send_message(message.chat.id, startBotMessage.message, reply_markup=keyboard)


@bot.message_handler(regexp='^паспорт\s*')
def get_bot_info(message):
    # Персона рандомная, или созданная преждевременно?
    # Если рандомная, возможно в ней хранить chat_id???
    persona = Persona.query\
        .get(users_services.get_user(message.chat.id).persona_id)
    print('passport')
    # a = random.randint(1, 10) * 20
    #
    # bot.send_message(message.chat.id, 'Сила:')
    # bot.send_message(message.chat.id, a)
    #
    # b = random.randint(10, 120)
    # bot.send_message(message.chat.id, 'Интеллект:')
    # bot.send_message(message.chat.id, b)
    #
    # c = random.randint(1, 10)
    # bot.send_message(message.chat.id, 'Ловкость:')
    # bot.send_message(message.chat.id, c)

    bot.send_message(
        message.chat.id,
        f"""     
*  Жим:*  {persona.strength} 
*  ICQ:*  {persona.intelligence}      
*  Бег:*  {persona.agility}
            """,
        parse_mode='MarkdownV2'
    )


#     bot.send_message(
#         message.chat.id,
#         f"""
#         ```
# _____________________________________
# |   Жим    |    ICQ     |   Бег     |
# |  {a}     |   {b}      |   {c}     |
# _____________________________________
#         ```
#         """,
#         parse_mode='MarkdownV2'
#     )


@bot.message_handler(content_types=["text"])
def handle_messages(message):
    user = users_services.get_user(message.chat.id)
    if user:

        optional_of_chosen_action = action_services \
            .get_actions_by_message_id_and_phrase(user.state_id, message.text)
        # There could be problems, when user types message, which fits several actions
        print(optional_of_chosen_action)
        if len(optional_of_chosen_action) == 1:
            chosen_action = optional_of_chosen_action[0]
            decision: UserDecision = user_decision_services.find_by_action_id(chosen_action.id)
            if decision is None:
                bot.send_message(message.chat.id,
                                 'Не знаю что сказать дальше....', )
                return
            try:
                user.state_id = decision.state_id

                nextStepMessage: BotMessage = BotMessage.query.get(decision.state_id)
                keyboard = generate_user_action(nextStepMessage)
                bot.send_message(message.chat.id,
                                 nextStepMessage.message,
                                 reply_markup=keyboard)
                db.session.commit()
            except Exception:
                db.session.rollback()
                raise
    else:
        bot.sende_message(message.chat.id, 'Кто это?! Уйди от меня!!!')


def generate_user_action(botMessage: BotMessage):
    keyboard = types.ReplyKeyboardMarkup()
    for action in botMessage.actions:
        keyboard.add(types.KeyboardButton(text=action.user_phrase))
    return keyboard
