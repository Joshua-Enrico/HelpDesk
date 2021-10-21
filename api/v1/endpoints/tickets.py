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
from sqlalchemy import func
import json


def jsonify_pagination(pagination):
    keys = ['has_next', 'has_prev',
            'next_num', 'page', 'pages', 'per_page',
            'prev_num', 'total']
    d = {}
    d['items'] = [r._asdict() for r in pagination.items]
    for k in keys:
        d[k] = pagination.__getattribute__(k)
    return jsonify(d)


@app_views.route('/admin/tickets/<int:page>', methods=['GET'], strict_slashes=False)
def get_Tickets(page=1):
    per_page = 10
    status_filter = request.args.get('status', None)
    pagination = db.session\
                   .query(Tickets.id, Tickets.Status, Tickets.Subject, Tickets.Company_Area, Tickets.DateTime,
                          (Users.Nombre + ' ' + Users.Apellido).label('Agent'))\
                   .join(Users, Users.id == Tickets.Agent_ID, isouter=True)\
                   .filter(True if status_filter is None else Tickets.Status == status_filter)\
                   .paginate(page, per_page, error_out=False)
    return jsonify_pagination(pagination)


@app_views.route('/admin/tickets/<ticket_id>', methods=['GET', 'PUT'], strict_slashes=False)
def get_update_ticket(ticket_id):
    ticket = Tickets.query.get(ticket_id)

    if ticket is None:
        abort(404)

    if request.method == 'GET':
        return jsonify(ticket.to_dict())

    if request.method == 'PUT':
        valid_attrs = ['Subject', 'Problem_Type', 'Description']
        new_values = request.get_json()
        if not request.get_json():
            abort(400, description="Not a JSON")

        for attr, val in new_values.items():
            if attr in valid_attrs:
                setattr(ticket, attr, val)

        db.session.commit()

        return jsonify(complete='Ticket Actualizado')


@app_views.route('/admin/tickets', methods=['POST'], strict_slashes=False)
def Create_Tickets():
    if not request.get_json():
        abort(400, description="Not a JSON")
    ticket = request.get_json()
    if (ticket):
        New_Ticket = Tickets(User_ID=ticket['User_id'], Subject=ticket['subject'], Problem_Type=ticket['problemType'], Company_Area=ticket['company_area'], Description=ticket['description'])
        db.session.add(New_Ticket)
        db.session.commit()
        summary = User_Tickets_Summary.query.filter_by(User_id=ticket['User_id']).first()
        all_summary = Tickets_Summary.query.first()
        if (all_summary == None):
            obj = Tickets_Summary(All_tickets=0, Pendings=0, Solved=0, Assigned=0)
            db.session.add(obj)
            db.session.commit()

        if (summary == None):
            User_Summary =  User_Tickets_Summary(All_tickets=1, Pendings=1, Assigned=0, Solved=0, User_id=ticket['User_id'])
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


    return jsonify(complete='Ticket Creado')
