#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
import sys
from web_flask.models.user import Users
from web_flask.models.tickets import Tickets
from web_flask.models.agent_tickets_summary import Agent_Tickets_Summary
from api.v1 import app_views
from flask import abort, jsonify, make_response, request
import json
from ..middlewares.isagent import isagent

@app_views.route('/agent_summary/<User_id>', methods=['GET'], strict_slashes=False)
@isagent
def get_agent_summary(User_id):
    new_dic = []
    objs = Agent_Tickets_Summary.query.filter_by(User_id=User_id).first()
    if objs is not None:
        new_dic.append(objs.to_dict())
    return jsonify(new_dic)
