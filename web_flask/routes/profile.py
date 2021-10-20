#!/usr/bin/python3
from ..models import app
from ..functions.recover_account import recover_account_func
from ..functions.recover_pwd import recover_validations
from ..models.user import Users
from ..models.time_access import Time_Access
from flask import render_template





@app.route('/user_edit/<User_id>/', methods=['GET'] )
def user_edit_admin(User_id):
    new_dic = []
    User_data = Users.query.filter_by(id=User_id).first()
    User_time_acces = Time_Access.query.filter_by(User_id=User_id).first()
    User_time_acces.From = User_time_acces.From.strftime("%Y-%d-%m")
    User_time_acces.To = User_time_acces.To.strftime("%Y-%d-%m")
    print(User_data.id)
    print(User_data.Nombre)
    return render_template('Administrador/user_edit.html', id=User_id ,User_data=User_data, Time_Access=User_time_acces)
