#!/usr/bin/python3
from ...models import app
from ...models.user import Users
from ...models.time_access import Time_Access
from flask import render_template, redirect, url_for
from .Functions.access_validation import client_acces_val
from flask_login import login_required ,current_user
from datetime import datetime, timezone



@app.route('/user_profile/<User_id>/', methods=['GET'] )
@login_required
def profile_user(User_id):
    if (current_user.Rol != 'Usuario'):
        return redirect(url_for(client_acces_val(current_user.Rol)))
    new_dic = []
    User_data = Users.query.filter_by(id=User_id).first()
    User_time_acces = Time_Access.query.filter_by(User_id=User_id).first()
    User_time_acces.From = User_time_acces.From.strftime("%Y-%d-%m")
    User_time_acces.To = User_time_acces.To.strftime("%Y-%d-%m")

    L_login = User_time_acces.Last_login.replace(tzinfo=timezone.utc).astimezone(tz=None)
    Last_activity = User_time_acces.Last_activity.replace(tzinfo=timezone.utc).astimezone(tz=None)
    Create_at = User_data.DateTime.replace(tzinfo=timezone.utc).astimezone(tz=None)
    Modified_at = User_data.UpdateTime.replace(tzinfo=timezone.utc).astimezone(tz=None)

    User_data.DateTime = Create_at.strftime("%d/%m/%Y")
    User_data.UpdateTime = Modified_at.strftime("%d/%m/%Y")
    User_time_acces.Last_login = L_login.strftime("%d/%m/%Y a las %H:%M")
    User_time_acces.Last_activity = Last_activity.strftime("%d/%m/%Y a las %H:%M")
    return render_template('Usuario/user_profile.html', User_id=User_id ,User_data=User_data, Time_Access=User_time_acces)
