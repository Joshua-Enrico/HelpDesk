#!/usr/bin/python3
""" This module defines functions to authenticate users """
from api.utils import generate_token


@app_views.route('/token', methods=['POST'], strict_slashes=False)
def gen_token():
    body = request.as_json()
    if body is None:
        abort(400, 'Not a JSON')

    if body.get('key') != '!#7wyew2*$#2':
        abort(401, 'Not Authorized')


    user = body.get('user')
    return jsonify(generate_token(user))
