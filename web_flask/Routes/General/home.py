#!/usr/bin/python3
from ...models import app
from ...models.user import Users
from ...models.forms import login_manager
from .Functions.login import login_validations
from flask import render_template

@login_manager.user_loader
def load_user(User_id):
    return Users.query.get(str(User_id))


@app.route('/', methods=['GET', 'POST'])
def login():
    return login_validations()


@app.route('/login', methods=['GET', 'POST'])
def login_redirect():
    return login_validations()


@app.route('/landing', methods=['GET', 'POST'])
def landing():
    return render_template('General/landing.html')
