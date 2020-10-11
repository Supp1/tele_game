from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from telebot import TeleBot

from definitions import ROOT_DIR
from .config import API_TOKEN

bot = None
app = None
db = None


def create_app():
    global bot
    global app
    global db

    bot = TeleBot(API_TOKEN)
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{ROOT_DIR}/static/db/tele_game_prod.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db = SQLAlchemy(app)
    init_db()

    from .controllers import register_blueprints
    register_blueprints(app)

    return app


def init_db():
    from .models import user
    from .models import quest_models
    # db.drop_all()
    db.create_all()
