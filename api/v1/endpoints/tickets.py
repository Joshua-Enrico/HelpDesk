#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
import sys
from web_flask.models.user import Users
from web_flask.models.tickets import Tickets
from api.v1.endpoints import app_views
from flask import abort, jsonify, make_response, request
import json




@app_views.route('/tickets', methods=['GET'], strict_slashes=False)
def get_Tickets():
    new_dic = []
    objs = Tickets.query.all()
    for Ticket in objs:
        new_dic.append(Ticket.to_dict())
    print(new_dic)
    return jsonify(new_dic)
