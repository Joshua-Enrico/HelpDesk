from flask_login import UserMixin
from ..models import db
from ..models.base import BaseModel
from datetime import datetime

class Reviews(UserMixin, db.Model, BaseModel):
    """ Reviews table , the idea here is use it when necessary"""
    id = db.Column(db.Integer, primary_key=True)
    Text = db.Column(db.String(1000))
    Ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'))
    DateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
