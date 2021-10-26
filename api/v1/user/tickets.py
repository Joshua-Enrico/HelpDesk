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
                   .query(Tickets.id, Tickets.Status, Tickets.Service_Score, Tickets.Subject, Tickets.Company_Area, Tickets.DateTime,
                          (Users.Nombre + ' ' + Users.Apellido).label('Agent'))\
                   .join(Users, Users.id == Tickets.Agent_ID, isouter=True)\
                   .filter(Tickets.User_ID == user_id)\
                   .filter(True if status_filter is None else Tickets.Status == status_filter)\
                   .order_by(Tickets.Status, Tickets.DateTime.desc())\
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


@app_views.route('/user/tickets/<ticket_id>/rate_service', methods=['PUT'], strict_slashes=False)
def update_user_ticket(ticket_id):
    user = request.environ.get('user', {})
    user_id = user.get('id', None)
    ticket = Tickets.query\
                .filter(Tickets.User_ID == user_id)\
                .filter(Tickets.id == ticket_id)\
                .first()
    if ticket is None:
        abort(404)

    if ticket.Service_Score is not None:
        return jsonify({'success': False, 'msg': 'Este ticket ya ha sido calificado'}), 400

    if ticket.Status != 2:
        return jsonify({'success': False, 'msg': 'Para poder calificar, el ticket debe estar marcado como resuelto'}), 400

    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")

    required = [('Service_Score', 'calificación del servicio')]

    errors = {}
    for attr in required:
        if not data.get(attr[0]):
            errors[attr[0]] = 'El campo "{}" es requerido'.format(attr[1])
    if errors != {}:
        return jsonify({'success': False, 'errors':errors}), 400

    service_score = str(data.get('Service_Score', ''))
    if not service_score.isdigit():
        return jsonify({'success': False, 'msg': 'La calificación debe ser un valor numérico'}), 400

    score = int(service_score)
    if score < 1 or score > 10:
        return jsonify({'success': False, 'msg': 'La calificación debe ser un valor numérico entre 1 y 10'}), 400

    ticket.Service_Score = data.get('Service_Score')
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

    """ Actualizando actividad de usuario y tablas de resumen  """
    user_time_access = Time_Access.query.filter_by(User_id=user.get('id')).first()
    user_time_access.Last_activity = datetime.utcnow()
    summary = User_Tickets_Summary.query.filter_by(User_id=user.get('id')).first()
    all_summary = Tickets_Summary.query.first()
    print(all_summary)
    if (all_summary == None):
        obj = Tickets_Summary(All_tickets=0, Pendings=0, Solved=0, Assigned=0)
        db.session.add(obj)
        db.session.commit()

    if (summary == None):
        User_Summary =  User_Tickets_Summary(All_tickets=1, Pendings=1, Assigned=0, Solved=0, User_id=user.get('id'))
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

    return jsonify({'id': newticket.id}), 200
