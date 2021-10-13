#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
import sys
from web_flask.models.Class import Users, Tickets, User_Tickets_Summary
from api_v1.v1.endpoints import app_views
from flask import abort, jsonify, make_response, request
import json




@app_views.route('/user_summary/<User_id>', methods=['GET'], strict_slashes=False)
def get_user_summary(User_id):
    new_dic = []
    objs = User_Tickets_Summary.query.filter_by(User_id=User_id).first()
    new_dic.append(objs.to_dict())
    print(new_dic)
    return jsonify(new_dic)