from datetime import datetime
from flask import Flask, request
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer
import os
import pymysql
import smtplib

# time = "%Y-%m-%dT%H:%M:%S.%f"
app = Flask(__name__, template_folder='../Static/templates', static_folder='../Static')
Bootstrap(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = "testing"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Helpdesk:Helpdesk@localhost/HelpDesk'
app.url_map.strict_slashes = False
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
socketio = SocketIO(app, cors_allowed_origins='*')
db = SQLAlchemy(app, session_options={"autoflush": False})



