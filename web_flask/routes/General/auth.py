#!/usr/bin/python3
from ...models import app
from .Functions.signup import signup_validations
from flask import redirect, url_for
from flask_login import login_required
from flask_login import logout_user


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """ We call validation function where we have all render an validations to do"""
    return signup_validations()


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
