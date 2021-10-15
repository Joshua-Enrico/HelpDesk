from flask_login import UserMixin
from ..models import db
from ..models.base import BaseModel
from ..models.reviews import Reviews
from datetime import datetime
import uuid

class Tickets(UserMixin, db.Model, BaseModel):
    """ Tickets Table """
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
