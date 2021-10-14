#!/usr/bin/python3
from ..models import app
from ..functions.confirmed import confirmed_func

@app.route('/confirm_email/<token>/<user_id>', methods=['GET', 'POST'] )
def confirmed(token, user_id):
    return  confirmed_func(token, user_id)
