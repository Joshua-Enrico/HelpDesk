from web_flask.models import db
from web_flask.models.agent_tickets_summary import *
from web_flask.models.reviews import *
from web_flask.models.tickets import *
from web_flask.models.tickets_summary import *
from web_flask.models.time_access import *
from web_flask.models.user import *
from web_flask.models.user_tickets_summary import *
from web_flask.models.workers_ids import *
from werkzeug.security import generate_password_hash

db.create_all()
