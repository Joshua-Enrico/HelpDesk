#!/usr/bin/python3
from ..models import app
from ..models.forms.create_user import CreateUser
from flask_login import login_required
from flask import render_template
import datetime
import uuid

@app.route("/administracion_usuario", methods=['GET', 'POST'])
@login_required
def User_Administration():
    form = CreateUser()
    flag = 0
    User_Exists = ''
    Email_Exist = ''
    Not_equal = ''
    Wrong_date = ''
    Rol_validation = ''
    Area_validation = ''


    if form.validate_on_submit():
        user = Users.query.filter_by(Username=form.Username.data).first()
        if (user):
            flag = 1
            User_Exists='El Nombre De Usuario Ya existe'
        Email = Users.query.filter_by(Email=form.Email.data).first()
        
        if(Email):
            flag = 1
            Email_Exist = 'El Correo Ya Existe'

        if (form.Password.data != form.Confirmed_Password.data):
            print("diferent")
            flag = 1
            Not_equal='Las contraseñas no son iguales'
        now = datetime.date.today()
        if (form.Desde.data < now):
            flag = 1
            Wrong_date='Las Fechas tienes que ser mayor a la actual'

        if (form.Area.data == 'Seleccionar'):
            flag = 1
            Area_validation = 'Debe Seleccionar Un Area'

        if (form.Rol.data == 'Seleccionar'):
            flag = 1
            Rol_validation = 'Debe Seleccionar Un Rol Valido'

        if(form.Desde.data > form.Hasta.data):
            flag = 1
            Wrong_date='Las Fechas no son validas'
        if (flag != 0):
            return render_template(
            'administrador/administracion_usuario.html',
            form=form,
            Wrong_date=Wrong_date,
            Not_equal=Not_equal,
            Email_Exist=Email_Exist,
            User_Exists=User_Exists,
            Rol_validation=Rol_validation,
            Area_validation=Area_validation)

        hashed_paswrd = generate_password_hash(form.Password.data, method='sha256')
        new_user = Users(
            id=str(uuid.uuid4()),
            Username=form.Username.data,
            Nombre=form.Nombre.data,
            Apellido=form.Apellido.data,
            Email=form.Email.data,
            Password=hashed_paswrd,
            Rol=form.Rol.data,
            Area=form.Area.data,
            Estado='Activo')

        Access_Time = Time_Access(id=str(uuid.uuid4()), User_id=new_user.id, From=form.Desde.data, To=form.Hasta.data)
        db.session.add(new_user)
        db.session.add(Access_Time)
        db.session.commit()
        print(new_user.id)
        return render_template('administrador/administracion_usuario.html', form=form, complete='Usuario Creado Correctamente')

    return render_template('administrador/administracion_usuario.html', form=form)
