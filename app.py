from flask_restx import Api
from flask import Flask
from config import Config
from dao.model.users import User
from setup_db import db
from views.auth import auth_ns
from views.directors import directors_ns
from views.genres import genres_ns
from views.movies import movies_ns
from views.users import users_ns


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    return application


def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(users_ns)
    api.add_namespace(auth_ns)
    #create_data(application, db)


# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#
#         u1 = User(username="vasya", password="my_little_pony", role="user")
#         u2 = User(username="ivan", password="qwerty", role="user")
#         u3 = User(username="oleg", password="P@ssw0rd", role="admin")
#
#         with db.session.begin():
#             db.session.add_all([u1, u2, u3])


app = create_app(Config())

if __name__ == "__main__":

    app.run()

