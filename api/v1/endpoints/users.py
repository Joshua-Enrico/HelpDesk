#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
import sys
from web_flask.models.user import Users
from web_flask.models.time_access import Time_Access
from web_flask.models.forms.create_user import CreateUser
from web_flask.models import db
from werkzeug.security import generate_password_hash
from api.v1.endpoints import app_views
from flask import abort, jsonify, make_response, request
import json
from datetime import datetime
import datetime as current
import uuid





@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    new_dic = []
    objs = Users.query.all()
    for user in objs:
        new_dic.append(user.to_dict())
    return jsonify(new_dic)


@app_views.route('/users/', methods=['POST'], strict_slashes=False)
def create_user():
    flag = 0
    User_Exists = ''
    Email_Exist = ''
    Not_equal = ''
    Wrong_date = ''
    Rol_validation = ''
    Area_validation = ''
    if not request.get_json():
        abort(400, description="Not a JSON")
    form = request.get_json()
    if (form):
        user = Users.query.filter_by(Username=form['Username']).first()
        if (user):
            flag = 1
            User_Exists='El Nombre De Usuario Ya existe'
        Email = Users.query.filter_by(Email=form['Email']).first()
        if(Email):
            flag = 1
            Email_Exist = 'El Correo Ya Existe'
        print(form['Desde'])
        if (form['Password'] != form['Confirmed_Password']):
            print("diferent")
            flag = 1
            Not_equal='Las contraseñas no son iguales'
        if(form['Desde'] == '' or form['Hasta'] == ''):
            flag = 1
            Wrong_date='Debes Seleccionar Una Fecha En Ambos Campos'
        if(form['Desde'] != '' and form['Hasta'] != ''):
            now = current.date.today()
            date_time_obj = datetime.strptime(form['Desde'], '%Y-%m-%d').date()
            print(type(date_time_obj))
            if (date_time_obj < now):
                flag = 1
                Wrong_date='Las Fechas tienen que ser mayor a la actual'
            Desde = datetime.strptime(form['Desde'], '%Y-%m-%d').date()
            Hasta = datetime.strptime(form['Hasta'], '%Y-%m-%d').date()
            if(Desde > Hasta):
                flag = 1
                Wrong_date='Las Fechas no son validas'

        if (form['Area'] == 'Seleccionar'):
            flag = 1
            Area_validation = 'Debe Seleccionar Un Area'

        if (form['Rol'] == 'Seleccionar'):
            flag = 1
            Rol_validation = 'Debe Seleccionar Un Rol Valido'

        if (flag != 0):
            return jsonify(
            Wrong_date=Wrong_date,
            Not_equal=Not_equal,
            Email_Exist=Email_Exist,
            User_Exists=User_Exists,
            Rol_validation=Rol_validation,
            Area_validation=Area_validation)

        hashed_paswrd = generate_password_hash(form['Password'], method='sha256')
        new_user = Users(
            id=str(uuid.uuid4()),
            Username=form['Username'],
            Nombre=form['Nombre'],
            Apellido=form['Apellido'],
            Email=form['Email'],
            Password=hashed_paswrd,
            Rol=form['Rol'],
            Area=form['Area'],
            Estado='Activo')

        Access_Time = Time_Access(id=str(uuid.uuid4()), User_id=new_user.id, From=form['Desde'], To=form['Hasta'], Last_activity=datetime.utcnow(), Last_login=datetime.utcnow())
        db.session.add(new_user)
        db.session.add(Access_Time)
        db.session.commit()
        print(new_user.id)
        return jsonify(
            complete='Usuario Creado Corectamente',
            Wrong_date=Wrong_date,
            Not_equal=Not_equal,
            Email_Exist=Email_Exist,
            User_Exists=User_Exists,
            Rol_validation=Rol_validation,
            Area_validation=Area_validation)
