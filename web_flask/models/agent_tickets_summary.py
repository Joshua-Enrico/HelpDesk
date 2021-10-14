from flask_login import UserMixin
from ..models import db
from ..models.base import BaseModel
from datetime import datetime

class Agent_Tickets_Summary(UserMixin, db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    All_tickets = db.Column(db.Integer)
    Pendings = db.Column(db.Integer)
    Solved = db.Column(db.Integer)
    User_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    DateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
