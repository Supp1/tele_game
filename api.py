import telebot
import random
from telebot import types
import threading

bot = telebot.TeleBot('1231129772:AAG_jgw3O8dxG374MTZg8MtHMNMXVvZH9rw')


@bot.message_handler(content_types=["text"])
def handle_messages(message):
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
    win_or_lose = random.randint(1, 2)
    if message.text == 'Чего?' and win_or_lose == 1:
        keyboard_hider = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Ничего', reply_markup=keyboard_hider)
    elif message.text == 'Чего?' and win_or_lose == 2:
        keyboard_hider = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Ты проиграл паренёчек', reply_markup=keyboard_hider)


if __name__ == '__main__':
    bot.polling(none_stop=True)
