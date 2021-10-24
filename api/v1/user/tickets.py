#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from api.utils import jsonify_pagination
from api.v1 import app_views
from datetime import datetime
from flask import abort, jsonify, make_response, request
from web_flask.models.user import Users
from web_flask.models.tickets import Tickets
from web_flask.models.time_access import Time_Access
from web_flask.models import db
from web_flask.models.user_tickets_summary import User_Tickets_Summary
from web_flask.models.tickets_summary import Tickets_Summary
from web_flask.models.user import Users
from sqlalchemy import func
import json


@app_views.route('/user/tickets', methods=['GET'], strict_slashes=False)
def user_tickets():
    user = request.environ.get('user', {})
    user_id = user.get('id', None)
    per_page = 10
    page = int(request.args.get('page', 1))
    status_filter = request.args.get('status', None)
    pagination = db.session\
                   .query(Tickets.id, Tickets.Status, Tickets.Subject, Tickets.Company_Area, Tickets.DateTime,
                          (Users.Nombre + ' ' + Users.Apellido).label('Agent'))\
                   .join(Users, Users.id == Tickets.Agent_ID, isouter=True)\
                   .filter(Tickets.User_ID == user_id)\
                   .filter(True if status_filter is None else Tickets.Status == status_filter)\
                   .order_by(Tickets.Status)\
                   .paginate(page, per_page, error_out=False)
    return jsonify_pagination(pagination)


@app_views.route('/user/tickets/<ticket_id>', methods=['GET'], strict_slashes=False)
def user_ticket(ticket_id):
    user = request.environ.get('user', {})
    user_id = user.get('id', None)
    ticket = Tickets.query\
                .filter(Tickets.User_ID == user_id)\
                .filter(Tickets.id == ticket_id)\
                .first()
    if ticket is None:
        abort(404)

    return jsonify(ticket.to_dict())


@app_views.route('/user/tickets/<ticket_id>/solved', methods=['PUT'], strict_slashes=False)
def update_user_ticket(ticket_id):
    user = request.environ.get('user', {})
    user_id = user.get('id', None)
    ticket = Tickets.query\
                .filter(Tickets.User_ID == user_id)\
                .filter(Tickets.id == ticket_id)\
                .first()
    if ticket is None:
        abort(404)

    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")

    required = [('Service_Score', 'calificación del servicio')]

    errors = {}
    for attr in required:
        if not data.get(attr[0]):
            errors[attr[0]] = 'El campo "{}" es requerido'.format(attr[1])
    if errors != {}:
        return jsonify(errors), 400

    allowed = ['Service_Score']
    [setattr(ticket, k, v) for k, v in data.items() if hasattr(ticket, k) and k in allowed]
    ticket.Status = 2
    db.session.commit()

    return jsonify({'id': ticket_id}), 200


@app_views.route('/user/tickets', methods=['POST'], strict_slashes=False)
def create_user_ticket():
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")

    required = [
        ('Subject', 'Título'),
        ('Problem_Type', 'Tipo de problema'),
        ('Description', 'Descripción')
    ]

    print(data)
    errors = {}
    for attr in required:
        if not data.get(attr[0]):
            errors[attr[0]] = 'El campo "{}" es requerido'.format(attr[1])
    if errors != {}:
        return jsonify(errors), 400

    user = request.environ.get('user', {})
    newticket = Tickets(User_ID=user.get('id'),
                         Subject=data['Subject'],
                         Problem_Type=data['Problem_Type'],
                         Company_Area=user.get('area', None),
                         Description=data['Description'])
    db.session.add(newticket)
    db.session.commit()

    return jsonify({'id': newticket.id}), 200
