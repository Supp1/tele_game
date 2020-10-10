import random
from telebot import TeleBot, types
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker

WEBHOOK_LISTEN = "0.0.0.0"
WEBHOOK_PORT = 8443
CLIENT_ID = 'gp762nuuoqcoxypju8c569th9wz7q5'
TWITCH_AUTH_TOKEN = 'Bearer 984zuraizg1z1ppuwwqva7kkxrqso6'

API_TOKEN = '1231129772:AAG_jgw3O8dxG374MTZg8MtHMNMXVvZH9rw'
bot = TeleBot(API_TOKEN)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/db/tele_game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

Session = sessionmaker()
Session.configure(bind=db.engine)
session = Session()


class HighlightClip(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    url = db.Column(db.String(500))
    state = db.Column(db.Boolean())

    def __repr__(self):
        return f'<Clip {self.id}, {self.url}, {self.state}'


class TgUser(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    chat_id = db.Column(db.Integer)

    def __repr__(self):
        return f'<Clip {self.id}, {self.url}, {self.state}'


@bot.message_handler(commands=["start"])
def send_welcome(message):
    print('hhhh')
    bot.send_message(message.chat.id, "Hi, i am Highlighter bot. ")


@bot.message_handler(commands=['enable'])
def enable_subscribe(message):
    if TgUser.query.filter_by(chat_id=message.chat.id).first() is not None:
        bot.send_message(message.chat.id, "You have been subscribed already")
        return
    user = TgUser(chat_id=message.chat.id)
    db.session.add(user)
    db.session.commit()
    bot.send_message(message.chat.id, "Success")


@bot.message_handler(commands=['disable'])
def disable_subscribe(message):
    if TgUser.query.filter_by(chat_id=message.chat.id).first() is None:
        bot.send_message(message.chat.id, "You haven't subscribed yet")
        return
    TgUser.query.filter(TgUser.chat_id == message.chat.id).delete()
    db.session.commit()
    bot.send_message(message.chat.id, "Success")


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


# @bot.message_handler(commands=["help"])
# def send_help(message):
#     bot.send_message(message.chat.id, '', parse_mode="Markdown")

if __name__ == '__main__':
    app.run(debug=True, host=WEBHOOK_LISTEN, port=WEBHOOK_PORT)
    db.create_all()
    print('hh')
    bot.polling(none_stop=True)
