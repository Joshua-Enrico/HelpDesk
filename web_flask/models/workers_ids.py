from flask_login import UserMixin
from ..models import db
from ..models.base import BaseModel

class Workers_ids(UserMixin, db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.String(15), unique=True)
    Used = db.Column(db.String(15))
    Admin = db.Column(db.String(15))
    DateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
