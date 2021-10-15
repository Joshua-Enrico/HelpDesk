from flask_login import UserMixin
from ..models import db
from ..models.base import BaseModel
from datetime import datetime
import uuid

class User_Tickets_Summary(UserMixin, db.Model, BaseModel):
    id = db.Column(db.String(60), primary_key=True, default=uuid.uuid4)
    All_tickets = db.Column(db.Integer)
    Pendings = db.Column(db.Integer)
    Assigned =  db.Column(db.Integer)
    Solved = db.Column(db.Integer)
    User_id = db.Column(db.String(60), db.ForeignKey('users.id'))
    DateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
