from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'contact_model.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)
from contact_model.app_v1 import app_v1_bp, api_v1
from contact_model.homepage import app_hp_bp, api_hp
app.register_blueprint(app_v1_bp, url_prefix='/api/v1')
app.register_blueprint(app_hp_bp)
