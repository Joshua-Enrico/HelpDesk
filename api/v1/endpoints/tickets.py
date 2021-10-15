#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
import sys
from web_flask.models import db
from web_flask.models.user import Users
from web_flask.models.tickets import Tickets
from web_flask.models.user import Users
from api.v1.endpoints import app_views
from flask import abort, jsonify, make_response, request
import json


@app_views.route('/admin/tickets', methods=['GET'], strict_slashes=False)
def get_Tickets():
    new_dic = []
    objs = db.session.query(Tickets, Users).all()
    for Ticket, User in objs:
        d = Ticket.to_dict()
        d['Agent'] = '{} {}'.format(User.Nombre, User.Apellido)
        new_dic.append(d)
        print(Ticket.to_dict())
    
    return jsonify(new_dic)
