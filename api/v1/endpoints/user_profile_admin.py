#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
import sys
from web_flask.models.user import Users
from web_flask.models.time_access import Time_Access
from web_flask.models import db
from werkzeug.security import generate_password_hash, check_password_hash
from api.v1.endpoints import app_views
from flask import abort, jsonify, make_response, request
import json
from datetime import datetime
import datetime as current
import uuid

@app_views.route('/users_profile/', methods=['PUT'], strict_slashes=False)
def user_profile_admin():
    flag = ''
    Email_Exist = ''
    Not_equal = ''
    Wrong_date = ''
    Wrong_From= ''
    Wrong_To= ''
    User_Exists = ''
    now = current.date.today()


    if not request.get_json():
        abort(400, description="Not a JSON")

    form = request.get_json()
    User_id = form['User_id']
    Update_user = Users.query.filter_by(id=User_id).first()
    User_time_acces = Time_Access.query.filter_by(User_id=User_id).first()

    if(Update_user):
        if(form['From'] != ''):
            new_from = datetime.strptime(form['From'], '%Y-%m-%d').date()
            if(new_from < now):
                flag = 1
                Wrong_From='La Fecha Tiene Que ser Mayor A la Actual'
                return jsonify(
                Wrong_date=Wrong_date,
                Not_equal=Not_equal,
                Email_Exist=Email_Exist,
                User_Exists=User_Exists,
                Wrong_From=Wrong_From,
                Wrong_To=Wrong_To)
            else:
                print(User_time_acces.From)
                User_time_acces.From = Form['From']
                print(User_time_acces.From)

        if(form['To'] != ''):
            new_to = datetime.strptime(form['To'], '%Y-%m-%d').date()
            if(new_to < now):
                flag = 1
                Wrong_To ='La Fecha Tiene Que ser Mayor A la Actual'
                return jsonify(
                Wrong_date=Wrong_date,
                Not_equal=Not_equal,
                Email_Exist=Email_Exist,
                User_Exists=User_Exists,
                Wrong_From=Wrong_From,
                Wrong_To=Wrong_To)
            if(new_from):
                if(new_from > new_to):
                    flag = 1
                    Wrong_date= 'Las Fechas no son validas'
                    return jsonify(
                    Wrong_date=Wrong_date,
                    Not_equal=Not_equal,
                    Email_Exist=Email_Exist,
                    User_Exists=User_Exists,
                    Wrong_From=Wrong_From,
                    Wrong_To=Wrong_To)
                if(new_from == new_to):
                    flag = 1
                    Wrong_date= 'Las Fechas tiene que tener mas de un dia de diferencia'
                    return jsonify(
                    Wrong_date=Wrong_date,
                    Not_equal=Not_equal,
                    Email_Exist=Email_Exist,
                    User_Exists=User_Exists,
                    Wrong_From=Wrong_From,
                    Wrong_To=Wrong_To)
        if(form['Username'] != ''):
            validate = Users.query.filter_by(Username=form['Username']).first()
            print(validate.Username)
            if(validate):
                flag = 1
                if(form['Username'] == validate.Username):
                    User_Exists = 'Ya estas usando este nombre de usuario'
                else:
                    User_Exists = 'El usuario ya existe'

                return jsonify(
                Wrong_date=Wrong_date,
                Not_equal=Not_equal,
                Email_Exist=Email_Exist,
                User_Exists=User_Exists,
                Wrong_From=Wrong_From,
                Wrong_To=Wrong_To)
            else:
                new_username = form['Username']

        if(form['Email'] != ''):
            validate = Users.query.filter_by(Email=form['Email']).first()
            if(validate):
                flag = 1
                if(form['Email'] == validate.Email):
                    Email_Exist = 'Ya estas Usando Este Coreo'
                else:
                    Email_Exist = 'El Correo Ya Existe'

                return jsonify(
                Wrong_date=Wrong_date,
                Not_equal=Not_equal,
                Email_Exist=Email_Exist,
                User_Exists=User_Exists,
                Wrong_From=Wrong_From,
                Wrong_To=Wrong_To)
    else:
        return jsonify('hola')