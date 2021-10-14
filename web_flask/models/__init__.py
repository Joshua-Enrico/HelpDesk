from datetime import datetime
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer
import os
import pymysql
import smtplib

# time = "%Y-%m-%dT%H:%M:%S.%f"
app = Flask(__name__, template_folder='../functions/templates', static_folder='../static')
Bootstrap(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = "testing"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Helpdesk:Helpdesk@localhost/HelpDesk'
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

db = SQLAlchemy(app)
