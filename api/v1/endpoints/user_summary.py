#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
import sys
from web_flask.models.user import Users
from web_flask.models.tickets import Tickets
from web_flask.models.user_tickets_summary import User_Tickets_Summary
from api.v1.endpoints import app_views
from flask import abort, jsonify, make_response, request
import json




@app_views.route('/user_summary/<User_id>', methods=['GET'], strict_slashes=False)
def get_user_summary(User_id):
    new_dic = []
    objs = User_Tickets_Summary.query.filter_by(User_id=User_id).first()
    new_dic.append(objs.to_dict())
    print(new_dic)
    return jsonify(new_dic)
