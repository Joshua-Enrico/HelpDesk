#!/usr/bin/python3
from ..models import app
from ..functions.recover_account import recover_account_func
from ..functions.recover_pwd import recover_validations


@app.route('/recover', methods=['GET', 'POST'])
def recover_pwd():
    return recover_validations()


@app.route('/recover_acount/<token>/<Email>/<password>', methods=['GET', 'POST'] )
def recover_account(token, Email, password):
    return recover_account_func(token, Email, password)
