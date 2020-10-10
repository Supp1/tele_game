from .api_bot_control import bp


def register_blueprints(app):
    app.register_blueprint(bp)
