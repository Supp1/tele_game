from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from telebot import TeleBot

from definitions import ROOT_DIR
from .config import API_TOKEN

db = SQLAlchemy()

bot = TeleBot(API_TOKEN)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{ROOT_DIR}/static/db/tele_game.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    with app.app_context():
        init_db()

    from .controllers import register_blueprints
    register_blueprints(app)

    return app


def init_db():
    from .models import users
    from .models import quest_models
    db.create_all()
