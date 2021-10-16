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
    objs = db.session.query(Tickets, Users).all()
    for Ticket, User in objs:
        d = Ticket.to_dict()
        d['Agent'] = '{} {}'.format(User.Nombre, User.Apellido)
        new_dic.append(d)
    
    return jsonify(new_dic)

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
