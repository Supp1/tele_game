import random
from telebot import types

from app import bot


#       Process new update
def trigger_controls(updates):
    update = types.Update.de_json(updates)
    bot.process_new_updates([update])


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_animation(message.chat.id, "https://gph.is/g/ZdX9B61")
    bot.send_message(message.chat.id, "Hi, i am Highlighter bot.")


@bot.message_handler(content_types=["text"])
def handle_messages(message):
    win_or_lose = random.randint(1, 2)
    if message.text == 'Hello':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Пойти туда")
        button_geo = types.KeyboardButton(text="Пойти сюда")
        keyboard.add(button_phone, button_geo)
        bot.send_message(message.chat.id, 'Шо, куда пойдёшь?', reply_markup=keyboard)
    if message.text == 'Пойти сюда':
        keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button2 = types.KeyboardButton(text="И где я?")
        button1 = types.KeyboardButton(text="Чего?")
        keyboard1.add(button1, button2)
        bot.send_message(message.chat.id, 'И шо дальше?', reply_markup=keyboard1)
    if message.text == 'Чего?' and win_or_lose == 1:
        keyboard_hider = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Ничего', reply_markup=keyboard_hider)
    elif message.text == 'Чего?' and win_or_lose == 2:
        keyboard_hider = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Ты проиграл паренёчек', reply_markup=keyboard_hider)
