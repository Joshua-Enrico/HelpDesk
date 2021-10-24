#!/usr/bin/python3
""" objects that handle all default RestFul API actions for HelpDesk Agents """
from api.utils import jsonify_pagination
from api.v1 import app_views
from datetime import datetime
from flask import abort, jsonify, make_response, request
from web_flask.models.user import Users
from web_flask.models.tickets import Tickets
from web_flask.models.time_access import Time_Access
from web_flask.models import db
from web_flask.models.user import Users
from sqlalchemy import func
import json
from ..middlewares.isagent import isagent


@app_views.route('/agent/tickets', methods=['GET'], strict_slashes=False)
@isagent
def agent_tickets():
    user = request.environ.get('user', {})
    agent_id = user.get('id', None)
    per_page = 10
    page = int(request.args.get('page', 1))
    status_filter = request.args.get('status', None)
    pagination = db.session\
                   .query(Tickets.id, Tickets.Status, Tickets.Status, Tickets.Subject, Tickets.Company_Area, Tickets.DateTime,
                          (Users.Nombre + ' ' + Users.Apellido).label('Agent'))\
                   .join(Users, Users.id == Tickets.Agent_ID, isouter=True)\
                   .filter(Tickets.Agent_ID == agent_id or Tickets.Status.in_([0, None]))\
                   .filter(True if status_filter is None else Tickets.Status == status_filter)\
                   .order_by(Tickets.Status, Tickets.DateTime)\
                   .paginate(page, per_page, error_out=False)
    return jsonify_pagination(pagination)


@app_views.route('/agent/tickets/<ticket_id>', methods=['GET'], strict_slashes=False)
@isagent
def agent_ticket(ticket_id):
    user = request.environ.get('user', {})
    agent_id = user.get('id', None)
    ticket = Tickets.query\
                .filter(Tickets.id == ticket_id)\
                .first()
    if ticket is None:
        abort(404)

    return jsonify(ticket.to_dict())


@app_views.route('/agent/tickets/<ticket_id>/assign', methods=['PUT'], strict_slashes=False)
@isagent
def update_agent_ticket(ticket_id):
    user = request.environ.get('user', {})
    agent_id = user.get('id', None)
    ticket = Tickets.query\
                .filter(Tickets.Status.in_([None, 0]))\
                .filter(Tickets.id == ticket_id)\
                .first()
    if ticket is None:
        abort(404)

    ticket.Status = 1
    ticket.Agent_ID = agent_id
    db.session.commit()

    return jsonify({'id': ticket_id}), 200
