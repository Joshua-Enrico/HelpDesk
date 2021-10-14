#!/usr/bin/python3
from flask_login import LoginManager
from .. import app

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'