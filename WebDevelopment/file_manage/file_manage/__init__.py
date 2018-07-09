#coding:utf-8

from flask import Flask

from sqlalchemy.exc import OperationalError, ProgrammingError
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.engine.url import make_url
from views import views

app = Flask(__name__)

def create_app():
    with app.app_context():
        # app.config.from_object()
        app.register_blueprint(views)
        return app