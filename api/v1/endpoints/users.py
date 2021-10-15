#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
import sys
from web_flask.models.user import Users
from web_flask.models.time_access import Time_Access
from api.v1.endpoints import app_views
from flask import abort, jsonify, make_response, request
import json




@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    new_dic = []
    objs = Users.query.all()
    for user in objs:
        new_dic.append(user.to_dict())
    print(new_dic)
    return jsonify(new_dic)

