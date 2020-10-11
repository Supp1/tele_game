from app import create_app
from app.config import WEBHOOK_PORT, WEBHOOK_LISTEN

if __name__ == "__main__":
    # python manage.py                      # shows available commands
    # python manage.py runserver --help     # shows available runserver options
    create_app().run(WEBHOOK_LISTEN, 443, debug=True)
