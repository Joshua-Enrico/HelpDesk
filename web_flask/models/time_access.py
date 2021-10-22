from flask_login import UserMixin
from ..models import db
from ..models.base import BaseModel
from ..models.reviews import Reviews
from datetime import datetime
import uuid

""" Data Base """
class Time_Access(UserMixin, db.Model, BaseModel):
    id = db.Column(db.String(60), primary_key=True, default=uuid.uuid4)
    User_id = db.Column(db.String(60), db.ForeignKey('users.id'))
    From = db.Column(db.DateTime, nullable=False)
    To = db.Column(db.DateTime, nullable=False)
    Last_activity = db.Column(db.DateTime, nullable=False)
    Last_login = db.Column(db.DateTime, nullable=False)
    DateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
