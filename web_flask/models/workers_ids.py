from flask_login import UserMixin
from ..models import db
from ..models.base import BaseModel
import uuid
from datetime import datetime

class Workers_ids(UserMixin, db.Model, BaseModel):
    id = db.Column(db.String(60), primary_key=True, default=uuid.uuid4)
    User_id = db.Column(db.String(60), unique=True)
    Used = db.Column(db.String(15))
    Admin = db.Column(db.String(15))
    DateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    UpdateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
