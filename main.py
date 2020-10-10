import flask_script

from app import create_app
from app.config import WEBHOOK_PORT, WEBHOOK_LISTEN

manager = flask_script.Manager(create_app)
# manager.add_command('init_db', db.create_all)

if __name__ == "__main__":
    # python manage.py                      # shows available commands
    # python manage.py runserver --help     # shows available runserver options
    create_app().run(WEBHOOK_LISTEN, WEBHOOK_PORT, debug=True)
