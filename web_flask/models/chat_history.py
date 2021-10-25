from flask_login import UserMixin
from ..models import db
from ..models.base import BaseModel
from datetime import datetime
from ..models.time_access import Time_Access
from ..models.user_tickets_summary import User_Tickets_Summary
from ..models.agent_tickets_summary import Agent_Tickets_Summary
import uuid

class chathistory(UserMixin, db.Model, BaseModel):
    id = db.Column(db.String(60), primary_key=True, default=uuid.uuid4)
    Ticket_id = db.Column(db.String(60))
    Agent_ID = db.Column(db.String(60))
    User_ID = db.Column(db.String(60))
    message = db.Column(db.Text)
    DateTime = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
