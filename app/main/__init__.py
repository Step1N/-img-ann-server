from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
import urllib
import os

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
user_name = os.getenv('DB_USER', "user_name")
user_password = os.getenv('DB_USER_PWD', "user_password")
db_name = os.getenv('DB_NAME', "db_name")
db_host = os.getenv('DB_HOST', "127.0.0.1")

mongo_url = "mongodb://"+user_name+":" + urllib.parse.quote(user_password) +"@"+db_host+":27017/"+db_name
mongo = PyMongo(uri=mongo_url)

def create_app(env):
    app = Flask(__name__)
    app.config.from_object(config_by_name[env])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    app.config["MONGO_URI"] = mongo_url
    mongo.init_app(app)
    return app
