#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
import sys
from web_flask.models.Class import Users
from api_v1.v1.endpoints import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/', methods=['GET'], strict_slashes=False)
def get_users():
    new_dic = {}
    objs = Users.query.all()
    print(objs)
    for obj in objs:
        key = obj.Nombre + obj.Apellido
        new_dic[key] = {'Nombre':obj.Nombre,'Apellido':obj.Apellido, 'id': obj.User_id}
    print(new_dic)
    return jsonify(new_dic)