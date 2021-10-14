#!/usr/bin/python3
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, TextAreaField, DateField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_required, logout_user, current_user, login_user
import os
from itsdangerous import URLSafeTimedSerializer
import pymysql
import smtplib
from datetime import datetime
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"
app = Flask(__name__, template_folder='../functions/templates', static_folder='../static')
Bootstrap(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = "testing"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Helpdesk:Helpdesk@localhost/HelpDesk'#create database and user
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

""" Forms """
class LoginForm(FlaskForm):
    username = StringField('', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('', validators=[InputRequired(), Length(min=0, max=80)])
    remember = BooleanField('Recordar sesion')

class TicketForm(FlaskForm):
    subject = StringField('Asunto', validators=[InputRequired(), Length(max=100)])
    description = TextAreaField('Descripcion', validators=[InputRequired(), Length(max=1000)])
    problemType = SelectField(
        'Tipo de Problema',
        choices=[
            ('Hardware', 'Hardware'),
            ('Software', 'Software'),
        ], validators=[InputRequired()]
    )
    company_area = SelectField(
        'Seleccione su Area',
        choices=[
            ('Recursos Humanos', 'Recursos Humanos'),
            ('Marketing', 'Marketing'),
            ('Gerencia', 'Gerencia'),
        ], validators=[InputRequired()]
    )
class RegisterForm(FlaskForm):
    email = StringField('Correo', validators=[InputRequired(), Email(message='Correo Invalido'), Length(max=50)])
    username = StringField('Nombre de Usuario', validators=[InputRequired(), Length(min=4, max=30)])
    nombre = StringField('Nombre', validators=[InputRequired(), Length( max=15)])
    apellido = StringField('Apellido', validators=[InputRequired(), Length( max=15)])
    user_id = StringField('Id personal', validators=[InputRequired(), Length(min=3, max=3)])
    password = PasswordField('Contraseña', validators=[InputRequired(), Length(min=6, max=80)])

class CreateID(FlaskForm):
    user_id = StringField('ID de usuario', validators=[InputRequired(), Length(min=3, max=3)])
    admin = StringField('Tipo De Usuario', validators=[InputRequired(), Length(min=3, max=3)])

class CreateUser(FlaskForm):
    Username = StringField('Nombre de Usuario Para Ingreso', validators=[InputRequired(), Length(min=4, max=30)])
    Email = StringField('Email', validators=[InputRequired(), Email(message='Correo Invalido'), Length(max=50)])
    Nombre = StringField('Nombre de Usuario', validators=[InputRequired(), Length(min=4, max=30)])
    Apellido = StringField('Apellido de Usuario', validators=[InputRequired(), Length(min=4, max=30)])
    Password = PasswordField('Contraseña', validators=[InputRequired(), Length(min=5, max=80)])
    Confirmed_Password = PasswordField('Confirmar Contraseña', validators=[InputRequired(), Length(min=5, max=80)])
    Area = SelectField(
        'Area del Nuevo Usuario',
        choices=[
            ('Seleccionar', 'Seleccionar'),
            ('Recursos Humanos', 'Recursos Humanos'),
            ('Marketing', 'Marketing'),
            ('Gerencia', 'Gerencia'),
            ('Logistica', 'Logistica'),
            ('Sistemas', 'Sistemas'),
            ('Otros', 'Otros'),
        ], validators=[InputRequired()]
    )
    Rol = SelectField(
        'Seleccion El Rol Del Usuario',
        choices=[
            ('Seleccionar', 'Seleccionar'),
            ('Usuario', 'Usuario'),
            ('Administrador', 'Administrador'),
            ('HelpDesk', 'HelpDesk'),
        ], validators=[InputRequired()]
    )
    Desde = DateField('Fecha de Inicio', format='%Y-%m-%d')
    Hasta = DateField('Fecha Fin', format='%Y-%m-%d')

class recover(FlaskForm):
    email = StringField('', validators=[InputRequired(), Email(message='Correo Invalido'), Length(max=50)])
    new_password = PasswordField('', validators=[InputRequired(), Length(min=6, max=80)])


""" Data Base """
class Time_Access(UserMixin, db.Model):
    id = db.Column(db.String(60), primary_key=True, default=uuid.uuid4)
    User_id = db.Column(db.String(60), db.ForeignKey('users.id'))
    From = db.Column(db.DateTime, nullable=False)
    To = db.Column(db.DateTime, nullable=False)
    DateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Users(UserMixin, db.Model):
    id = db.Column(db.String(60), primary_key=True, default=uuid.uuid4)
    Username = db.Column(db.String(30), unique=True)
    Nombre = db.Column(db.String(30))
    Apellido = db.Column(db.String(30))
    Email = db.Column(db.String(50), unique=True)
    Password = db.Column(db.String(300))
    Rol = db.Column(db.String(20))
    Area = db.Column(db.String(30))
    Estado = db.Column(db.String(30))
    User_id = db.Column(db.String(60), unique=True)
    Time_Acess = db.relationship('Time_Access', backref='Users', lazy=True, cascade="all, delete, delete-orphan")
    Tickets_Summary_User = db.relationship('User_Tickets_Summary', backref='Users', lazy=True, cascade="all, delete, delete-orphan")
    Tickets_Summary_Agent = db.relationship('Agent_Tickets_Summary', backref='Users', lazy=True, cascade="all, delete, delete-orphan")
    DateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def to_dict(self, save_sf=None):
        new_dict = self.__dict__.copy()
        if "DateTime" in new_dict:
            new_dict["DateTime"] = new_dict["DateTime"].strftime(time)
        if "UpdateTime" in new_dict:
            new_dict["UpdateTime"] = new_dict["UpdateTime"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if "Password" in new_dict:
            del new_dict["Password"]
        return new_dict

class Workers_ids(UserMixin, db.Model):
    id = db.Column(db.String(60), primary_key=True, default=uuid.uuid4)
    User_id = db.Column(db.String(60), unique=True)
    Used = db.Column(db.String(15))
    Admin = db.Column(db.String(15))
    DateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    def to_dict(self, save_sf=None):
        new_dict = self.__dict__.copy()
        if "DateTime" in new_dict:
            new_dict["DateTime"] = new_dict["DateTime"].strftime(time)
        if "UpdateTime" in new_dict:
            new_dict["UpdateTime"] = new_dict["UpdateTime"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

class User_Tickets_Summary(UserMixin, db.Model):
    id = db.Column(db.String(60), primary_key=True, default=uuid.uuid4)
    All_tickets = db.Column(db.Integer)
    Pendings = db.Column(db.Integer)
    Assigned =  db.Column(db.Integer)
    Solved = db.Column(db.Integer)
    User_id = db.Column(db.String(60), db.ForeignKey('users.id'))
    DateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    def to_dict(self, save_sf=None):
        new_dict = self.__dict__.copy()
        if "DateTime" in new_dict:
            new_dict["DateTime"] = new_dict["DateTime"].strftime(time)
        if "UpdateTime" in new_dict:
            new_dict["UpdateTime"] = new_dict["UpdateTime"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

class Agent_Tickets_Summary(UserMixin, db.Model):
    id = db.Column(db.String(60), primary_key=True, default=uuid.uuid4)
    All_tickets = db.Column(db.Integer)
    Pendings = db.Column(db.Integer)
    Solved = db.Column(db.Integer)
    User_id = db.Column(db.String(60), db.ForeignKey('users.id'))
    DateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    def to_dict(self, save_sf=None):
        new_dict = self.__dict__.copy()
        if "DateTime" in new_dict:
            new_dict["DateTime"] = new_dict["DateTime"].strftime(time)
        if "UpdateTime" in new_dict:
            new_dict["UpdateTime"] = new_dict["UpdateTime"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

""" Tickets Summary, show last month or last 15 days information  """
class Tickets_Summary(UserMixin, db.Model):
    id = db.Column(db.String(60), primary_key=True, default=uuid.uuid4)
    All_tickets = db.Column(db.Integer)
    Pendings = db.Column(db.Integer)
    Assigned = db.Column(db.Integer)
    Solved = db.Column(db.Integer)
    DateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    def to_dict(self, save_sf=None):
        new_dict = self.__dict__.copy()
        if "DateTime" in new_dict:
            new_dict["DateTime"] = new_dict["DateTime"].strftime(time)
        if "UpdateTime" in new_dict:
            new_dict["UpdateTime"] = new_dict["UpdateTime"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

""" Tickets Table """
class Tickets(UserMixin, db.Model):
    id = db.Column(db.String(60), primary_key=True, default=uuid.uuid4)
    Agent_ID = db.Column(db.String(60))
    User_ID = db.Column(db.String(60))
    Subject = db.Column(db.String(100))
    Description = db.Column(db.String(1000))
    Problem_Type = db.Column(db.String(100))
    Company_Area = db.Column(db.String(45))
    Service_Score = db.Column(db.Integer)
    Review = db.relationship('Reviews', backref='Tickets', lazy=True, cascade="all, delete, delete-orphan")
    """ Here is better use code status, have a list of it """
    Status = db.Column(db.Integer)
    DateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    def to_dict(self, save_sf=None):
        new_dict = self.__dict__.copy()
        if "DateTime" in new_dict:
            new_dict["DateTime"] = new_dict["DateTime"].strftime(time)
        if "UpdateTime" in new_dict:
            new_dict["UpdateTime"] = new_dict["UpdateTime"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

""" Reviews table , the idea here is use it when necessary"""
class Reviews(UserMixin, db.Model):
    id = db.Column(db.String(60), primary_key=True, default=uuid.uuid4)
    Text = db.Column(db.String(1000))
    Ticket_id = db.Column(db.String(60), db.ForeignKey('tickets.id'))
    DateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    def to_dict(self, save_sf=None):
        new_dict = self.__dict__.copy()
        if "DateTime" in new_dict:
            new_dict["DateTime"] = new_dict["DateTime"].strftime(time)
        if "UpdateTime" in new_dict:
            new_dict["UpdateTime"] = new_dict["UpdateTime"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict
