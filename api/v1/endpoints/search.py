#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
import sys
from web_flask.models import db
from web_flask.models.user import Users
from web_flask.models.tickets import Tickets
from web_flask.models.user_tickets_summary import User_Tickets_Summary
from web_flask.models.tickets_summary import Tickets_Summary
from web_flask.models.user import Users
from api.v1.endpoints import app_views
from flask import abort, jsonify, make_response, request
from datetime import datetime
import json


@app_views.route('/admin/tickets', methods=['GET'], strict_slashes=False)
def get_Tickets():
    new_dic = []
    if not request.get_json():
        abort(400, description="Not a JSON")
    ticket = request.get_json()
    
    return jsonify(new_dic)