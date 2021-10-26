#!/usr/bin/python3
""" objects that handle all default RestFul API actions for HelpDesk Agents """
from api.utils import jsonify_pagination
from api.v1 import app_views
from datetime import datetime
from sqlalchemy import or_
from flask import abort, jsonify, make_response, request
from web_flask.models.user import Users
from web_flask.models.tickets import Tickets
from web_flask.models.time_access import Time_Access
from web_flask.models import db
from web_flask.models.user import Users
from sqlalchemy import func
import json
from web_flask.models.user_tickets_summary import User_Tickets_Summary
from web_flask.models.tickets_summary import Tickets_Summary
from web_flask.models.agent_tickets_summary import Agent_Tickets_Summary

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
                   .filter(or_(Tickets.Agent_ID == agent_id, Tickets.Status.in_([0, None])))\
                   .filter(True if status_filter is None else Tickets.Status == status_filter)\
                   .order_by(Tickets.Status, Tickets.DateTime.desc())\
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


@app_views.route('/agent/tickets/<ticket_id>/solve', methods=['PUT'], strict_slashes=False)
@isagent
def solve_ticket(ticket_id):
    user = request.environ.get('user', {})
    agent_id = user.get('id', None)
    ticket = Tickets.query\
                .filter(Tickets.id == ticket_id)\
                .filter(Tickets.Agent_ID == agent_id)\
                .first()
    if ticket is None:
        abort(404)

    ticket.Status = 2
    db.session.commit()

    return jsonify({'id': ticket_id}), 200


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

    if ticket.Status != 0 and ticket.Status != None:
        return jsonify({'success': False, 'msg': 'Este ticket ya ha sido asignado a un agente'}), 403

    ticket.Status = 1
    ticket.Agent_ID = agent_id
    db.session.commit()



    """ Updating users activity """
    agent_time_access = Time_Access.query.filter_by(User_id=ticket.Agent_ID).first()
    agent_time_access.Last_activity = datetime.utcnow()


    user_sumamry = User_Tickets_Summary.query.filter_by(User_id=ticket.User_ID).first()
    agent_summary = Agent_Tickets_Summary.query.filter_by(User_id=ticket.Agent_ID).first()
    all_summary = Tickets_Summary.query.first()


    user_sumamry.Pendings -= 1
    user_sumamry.Assigned += 1
    all_summary.Pendings -= 1
    all_summary.Assigned += 1
    if(agent_summary == None):
        agent_table =  Agent_Tickets_Summary(All_tickets=1, Pendings=0, Assigned=1, Solved=0, User_id=ticket.Agent_ID)
        db.session.add(agent_table)
    else:
        agent_summary.All_tickets += 1
        agent_summary.Assigned += 1
    db.session.commit()



    return jsonify({'id': ticket_id}), 200
