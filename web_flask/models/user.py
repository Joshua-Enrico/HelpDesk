from flask_login import UserMixin
from ..models import db
from ..models.base import BaseModel
from datetime import datetime
from ..models.user_tickets_summary import User_Tickets_Summary
from ..models.agent_tickets_summary import Agent_Tickets_Summary

class Users(UserMixin, db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(15), unique=True)
    Nombre = db.Column(db.String(30))
    Apellido = db.Column(db.String(30))
    Email = db.Column(db.String(50), unique=True)
    Password = db.Column(db.String(300))
    Admin = db.Column(db.String(20))
    Confirmed_mail = db.Column(db.String(10))
    User_id = db.Column(db.String(15), unique=True)
    Tickets_Summary_User = db.relationship(User_Tickets_Summary, backref='Users', lazy=True, cascade="all, delete, delete-orphan")
    Tickets_Summary_Agent = db.relationship(Agent_Tickets_Summary, backref='Users', lazy=True, cascade="all, delete, delete-orphan")
    DateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
