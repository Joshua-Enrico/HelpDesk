#!/usr/bin/python3
from ..models import app
from ..models.forms.create_id import CreateID
from flask_login import login_required
from flask import render_template


@app.route("/administracion_usuario")
@login_required
def user_administration():
    form = CreateID()
    if form.validate_on_submit():
        user_id = Workers_ids.query.filter_by(User_id=form.user_id.data).first()
        if (user_id):
            return render_template('administracion_usuario.html', form=form, wrong_id='EL ID ya existe')
        else:
            new_user = Workers_ids(User_id=form.user_id.data, Used='false', Admin=form.admin.data)
            db.session.add(new_user)
            db.session.commit()
            return render_template('administracion_usuario.html', form=form, complete='ID Creado Correctamente')
    return render_template('administracion_usuario.html', form=form)
