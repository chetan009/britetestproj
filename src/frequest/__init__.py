from flask import Flask
from os import urandom
app = Flask(__name__)
app.config['SECRET_KEY']= urandom(24)
app.config['DB_FILE'] = '../db.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{0}'.format(app.config['DB_FILE'])
from .views import *
