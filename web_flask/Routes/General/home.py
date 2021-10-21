#!/usr/bin/python3
from ...models import app
from ...models.user import Users
from ...models.forms import login_manager
from .Functions.login import login_validations

@login_manager.user_loader
def load_user(User_id):
    return Users.query.get(str(User_id))


@app.route('/', methods=['GET', 'POST'])
def login():
    return login_validations()

@app.route('/login', methods=['GET', 'POST'])
def login_redirect():
    return login_validations()
