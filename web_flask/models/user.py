from flask_login import UserMixin
from ..models import db
from ..models.base import BaseModel
from datetime import datetime
from ..models.time_access import Time_Access
from ..models.user_tickets_summary import User_Tickets_Summary
from ..models.agent_tickets_summary import Agent_Tickets_Summary
import uuid

class Users(UserMixin, db.Model, BaseModel):
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
    Time_Acess = db.relationship(Time_Access, backref='Users', lazy=True, cascade="all, delete, delete-orphan")
    Tickets_Summary_User = db.relationship(User_Tickets_Summary, backref='Users', lazy=True, cascade="all, delete, delete-orphan")
    Tickets_Summary_Agent = db.relationship(Agent_Tickets_Summary, backref='Users', lazy=True, cascade="all, delete, delete-orphan")
    DateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)