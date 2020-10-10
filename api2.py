import requests
import random
from telebot import TeleBot, types
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker

WEBHOOK_LISTEN = "0.0.0.0"
WEBHOOK_PORT = 8080
API_TOKEN = '1231129772:AAG_jgw3O8dxG374MTZg8MtHMNMXVvZH9rw'
bot = TeleBot(API_TOKEN)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/db/tele_game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

Session = sessionmaker()
Session.configure(bind=db.engine)
session = Session()


# MAIN FUNCTION
@app.route('/<token>', methods=['POST'])
# process only requests with correct bot token
def handle(token):
    if token == bot.token:
        request_body_dict = request.json
        update = types.Update.de_json(request_body_dict)
        print(update.__repr__())
        bot.process_new_updates([update])
        #       Process new update
        return app.response_class(
            response='OK',
            status=200,
            mimetype='application/json'
        )
    else:
        return app.response_class(
            response='Error',
            status=403,
            mimetype='application/json'
        )


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_animation(message.chat.id, "https://gph.is/g/ZdX9B61")
    bot.send_message(message.chat.id, "Hi, i am Highlighter bot. ")


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
    db.create_all()
    app.run(debug=True, host=WEBHOOK_LISTEN, port=WEBHOOK_PORT)
