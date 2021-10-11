#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
import sys
from web_flask.models.Class import *
from api_v1.v1.endpoints import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/', methods=['GET'], strict_slashes=False)
def get_users():
    """
    Retrieves the list of all user objects
    or a specific user
    """
    all_users = storage.all(User).values()
    list_users = []
    for user in all_users:
        list_users.append(user.to_dict())
    return jsonify(list_users)