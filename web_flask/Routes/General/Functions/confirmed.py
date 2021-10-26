#!/usr/bin/python3
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm

def confirmed_func(token, user_id):
    if request.method == 'POST':
        update_user = Users.query.filter_by(User_id=user_id).first()
        token = s.dumps(update_user.Email, salt='email-confirm')

        link = url_for('confirmed', token=token, user_id=user_id, _external=True)
        message = '\nTu link de confirmacion es: {}'.format(link)
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("helpdesk.notificacions@gmail.com", "vwwgjfvxxlwseqlz")
        server.sendmail("helpdesk.notificacions@gmail.com", update_user.Email, message)
        return render_template('confirmed.html', message="Link De confirmacion Enviado, verifique su Correo")
    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)
        update_user = Users.query.filter_by(User_id=user_id).update({'Confirmed_mail':'yes'})
        db.session.commit()
        return render_template('confirmed.html', message="Email Confirmado Ya puede ingresar al Sistema" ,predict_content='<a class="btn btn-lg btn-primary btn-block" href="/login">Ingresar</a>')
    except (BadSignature, SignatureExpired):
        return render_template('confirmed.html', message="Link de Confirmacion Expirado, Reenvie Confirmacion", predict_content='<button class="btn btn-lg btn-primary btn-block" type="submit">Reenviar Confirmacion</button>')
