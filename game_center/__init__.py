# -*- coding:utf-8 -*-
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from pretty_logging import pretty_logger
from pretty_logging import logging
from flask_cors import CORS

from .config import Config

db = SQLAlchemy()
app = Flask(__name__)

cors = CORS(app, resources={r"/v1/*": {"origins": "*"}})

# config
app.config.from_object(Config)

# init ext
db.init_app(app)

# app router
with app.app_context():
    print("db url: {}".format(Config.SQLALCHEMY_DATABASE_URI))
    if current_app.config["DEBUG"] == True:
        pretty_logger.setLevel(logging.DEBUG)
    else:
        pretty_logger.setLevel(logging.INFO)

    from .views import gc_user
    app.register_blueprint(gc_user, url_prefix="/v1/user")

    from .views import gc_services
    app.register_blueprint(gc_services, url_prefix="/v1/service")

    from .views import gc_rooms
    app.register_blueprint(gc_rooms, url_prefix="/v1/room")
