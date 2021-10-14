from flask_login import UserMixin
from ..models import db
from ..models.base import BaseModel
from datetime import datetime

class Tickets_Summary(UserMixin, db.Model, BaseModel):
    """ Tickets Summary, show last month or last 15 days information  """
    id = db.Column(db.Integer, primary_key=True)
    All_tickets = db.Column(db.Integer)
    Pendings = db.Column(db.Integer)
    Assigned = db.Column(db.Integer)
    Solved = db.Column(db.Integer)
    DateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
