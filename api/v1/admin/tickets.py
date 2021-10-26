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
from ..middlewares.isadmin import isadmin

@app_views.route('/admin/tickets', methods=['GET'], strict_slashes=False)
@isadmin
def get_all_tickets(page=1):
    per_page = 10
    page = int(request.args.get('page', 1))
    status_filter = request.args.get('status', None)
    pagination = db.session\
                   .query(Tickets.id, Tickets.Status, Tickets.Subject, Tickets.Company_Area, Tickets.DateTime,
                          (Users.Nombre + ' ' + Users.Apellido).label('Agent'))\
                   .join(Users, Users.id == Tickets.Agent_ID, isouter=True)\
                   .filter(True if status_filter is None else Tickets.Status == status_filter)\
                   .order_by(Tickets.Status, Tickets.DateTime.desc())\
                   .paginate(page, per_page, error_out=False)
    return jsonify_pagination(pagination)


@app_views.route('/admin/tickets/<ticket_id>', methods=['GET'], strict_slashes=False)
@isadmin
def get_ticket(ticket_id):
    ticket = Tickets.query.get(ticket_id)
    if ticket is None:
        abort(404)

    return jsonify(ticket.to_dict())


@app_views.route('/admin/tickets/<ticket_id>', methods=['PUT'], strict_slashes=False)
@isadmin
def update_ticket(ticket_id):
    ticket = Tickets.query.get(ticket_id)
    if ticket is None:
        abort(404)

    if ticket.Status == 2:
        abort(403)

    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")

    required = [
        ('Subject', 'Título'),
        ('User_ID', 'Id de usuario'),
        ('Problem_Type', 'Tipo de problema'),
        ('Company_Area', 'Area de la compañía'),
        ('Description', 'Descripción')
    ]

    errors = {}
    for attr in required:
        if not data.get(attr[0]):
            errors[attr[0]] = 'El campo "{}" es requerido'.format(attr[1])
    if errors != {}:
        return jsonify(errors), 400

    allowed = ['User_ID', 'Agent_ID', 'Subject', 'Description',
               'Problem_Type', 'Company_Area']
    [setattr(ticket, k, v) for k, v in data.items() if hasattr(ticket, k) and k in allowed]

    ticket.Status = 0 if ticket.Agent_ID == None else 1

    db.session.commit()

    return jsonify({'id': ticket_id}), 200


@app_views.route('/admin/tickets', methods=['POST'], strict_slashes=False)
@isadmin
def create_tickets():
    ticket = request.get_json()
    if not ticket:
        abort(400, description="Not a JSON")

    required = [
        ('Subject', 'Título'),
        ('User_ID', 'Id de usuario'),
        ('Problem_Type', 'Tipo de problema'),
        ('Company_Area', 'Area de la compañía'),
        ('Description', 'Descripción')
    ]

    errors = {}
    for attr in required:
        if not ticket.get(attr[0]):
            errors[attr[0]] = 'El campo "{}" es requerido'.format(attr[1])
    if errors != {}:
        return jsonify(errors), 400

    New_Ticket = Tickets(User_ID=ticket['User_ID'], Subject=ticket['Subject'], Problem_Type=ticket['Problem_Type'], Company_Area=ticket['Company_Area'], Description=ticket['Description'])
    db.session.add(New_Ticket)
    db.session.commit()


    user_time_access = Time_Access.query.filter_by(User_id=ticket['User_ID']).first()
    user_time_access.Last_activity = datetime.utcnow()
    summary = User_Tickets_Summary.query.filter_by(User_id=ticket['User_ID']).first()
    all_summary = Tickets_Summary.query.first()
    if (all_summary == None):
        obj = Tickets_Summary(All_tickets=0, Pendings=0, Solved=0, Assigned=0)
        db.session.add(obj)
        db.session.commit()

    if (summary == None):
        User_Summary =  User_Tickets_Summary(All_tickets=1, Pendings=1, Assigned=0, Solved=0, User_id=ticket['User_ID'])
        db.session.add(User_Summary)

        """ updating all summary """
        all_summary.All_tickets += 1
        all_summary.Pendings += 1
        all_summary.UpdateTime = datetime.now()
        db.session.commit()
    else:
        """ updating user summary table """
        summary.All_tickets +=  1
        summary.Pendings +=  1
        summary.UpdateTime = datetime.now()
        """ updating all summary table """
        all_summary.All_tickets += 1
        all_summary.Pendings += 1
        all_summary.UpdateTime = datetime.now()
        db.session.commit()

    return jsonify({'id': New_Ticket.id}), 201


@app_views.route('/admin/tickets/summary', methods=['GET'], strict_slashes=False)
@isadmin
def get_ticket_all():
    new_dic = []
    objs = Tickets_Summary.query.first()
    new_dic.append(objs.to_dict())
    return jsonify(new_dic)
