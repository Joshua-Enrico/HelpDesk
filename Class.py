#!/usr/bin/python
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_required, logout_user, current_user, login_user
import os
from itsdangerous import URLSafeTimedSerializer
import pymysql
import smtplib
from datetime import datetime


class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Contraseña', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Recordar sesion')

class RegisterForm(FlaskForm):
    email = StringField('Correo', validators=[InputRequired(), Email(message='Correo Invalido'), Length(max=50)])
    username = StringField('Nombre de Usuario', validators=[InputRequired(), Length(min=4, max=15)])
    nombre = StringField('Nombre', validators=[InputRequired(), Length( max=15)])
    apellido = StringField('Apellido', validators=[InputRequired(), Length( max=15)])
    user_id = StringField('Id personal', validators=[InputRequired(), Length(min=3, max=3)])
    password = PasswordField('Contraseña', validators=[InputRequired(), Length(min=6, max=80)])

class CreateID(FlaskForm):
    user_id = StringField('ID de usuario', validators=[InputRequired(), Length(min=3, max=3)])
    admin = StringField('Admin?', validators=[InputRequired(), Length(min=3, max=3)])
class recover(FlaskForm):
    email = StringField('Correo', validators=[InputRequired(), Email(message='Correo Invalido'), Length(max=50)])
    user_id = StringField('ID de usuario', validators=[InputRequired(), Length(min=3, max=3)])
    new_password = PasswordField('Contraseña', validators=[InputRequired(), Length(min=6, max=80)])

app = Flask(__name__)
Bootstrap(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Helpdesk:Helpdesk@localhost/HelpDesk'#create database and user
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(15), unique=True)
    Nombre = db.Column(db.String(30))
    Apellido = db.Column(db.String(30))
    Email = db.Column(db.String(50), unique=True)
    Password = db.Column(db.String(300))
    Admin = db.Column(db.String(20))
    Confirmed_mail = db.Column(db.String(10))
    User_id = db.Column(db.String(15), unique=True)
    Tickets_Summary_User = db.relationship('User_Tickets_Summary', backref='Users', lazy=True, cascade="all, delete, delete-orphan")
    Tickets_Summary_Agent = db.relationship('Agent_Tickets_Summary', backref='Users', lazy=True, cascade="all, delete, delete-orphan")
    DateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Workers_ids(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.String(15), unique=True)
    Used = db.Column(db.String(15))
    Admin = db.Column(db.String(15))
    DateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

class User_Tickets_Summary(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    All_tickets = db.Column(db.Integer)
    Pendings = db.Column(db.Integer)
    Solved = db.Column(db.Integer)
    User_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    DateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

class Agent_Tickets_Summary(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    All_tickets = db.Column(db.Integer)
    Pendings = db.Column(db.Integer)
    Solved = db.Column(db.Integer)
    User_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    DateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

""" Tickets Summary, show last month or last 15 days information  """
class Tickets_Summary(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    All_tickets = db.Column(db.Integer)
    Pendings = db.Column(db.Integer)
    Solved = db.Column(db.Integer)
    DateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

""" Tickets Table """
class Tickets(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Agent_ID = db.Column(db.String(15))
    Subject = db.Column(db.String(100))
    Description = db.Column(db.String(1000))
    Problem_Type = db.Column(db.String(45))
    Company_Area = db.Column(db.String(45))
    Service_Score = db.Column(db.Integer)
    Review = db.relationship('Reviews', backref='Tickets', lazy=True, cascade="all, delete, delete-orphan")
    """ Here is better use code status, have a list of it """
    Status = db.Column(db.Integer)
    DateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

""" Reviews table , the idea here is use it when necessary"""
class Reviews(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Text = db.Column(db.String(1000))
    Ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'))
    DateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
