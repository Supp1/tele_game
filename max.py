import telebot
import random
from telebot import types
import threading

bot = telebot.TeleBot('1231129772:AAG_jgw3O8dxG374MTZg8MtHMNMXVvZH9rw')


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
        keyboard = types.InlineKeyboardMarkup()
        button2 = types.InlineKeyboardButton(text="Да", callback_data="yes")
        button1 = types.InlineKeyboardButton(text="Нет", callback_data="no")
        keyboard.add(button1, button2)
        keyboard_hider = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Lose', reply_markup=keyboard_hider)
        bot.send_message(message.chat.id, 'Ты проиграл паренёчек. Не хочется всё с нуля? Посмотри рекламку',
                         reply_markup=keyboard)
        global last_message
        last_message = message
    if message.text == 'шо':
        def mytimer():
            keyboard = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, 'Время вышло, Жак Фреско ушёл', reply_markup=keyboard)

        keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button2 = types.KeyboardButton(text="Огурцы")
        button1 = types.KeyboardButton(text="Помидоры")
        keyboard1.add(button1, button2)
        bot.send_message(message.chat.id, 'Загадка от жака фреско. На решение дается 30 секунд. Время пошло.',
                         reply_markup=keyboard1)
        global time
        time = threading.Timer(30, mytimer)
        time.start()
    if message.text == 'Огурцы':
        keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Не верно, Жак Фреско обиделся', reply_markup=keyboard)
        time.cancel()
    elif message.text == 'Помидоры':
        keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Верно, Жак Фреско рад', reply_markup=keyboard)
        time.cancel()


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "yes":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Тут типо реклама")
            keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            button_phone = types.KeyboardButton(text="Пойти туда")
            button_geo = types.KeyboardButton(text="Пойти сюда")
            keyboard.add(button_phone, button_geo)
            bot.send_message(last_message.chat.id, 'Шо, куда пойдёшь?', reply_markup=keyboard)
        if call.data == "no":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Ну ты дурачек. Ну и зря.")


if __name__ == '__main__':
    bot.polling(none_stop=True)
