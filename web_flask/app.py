#!/usr/bin/python3
from .models import app

from .Routes.Admin.dashboard_admin import *
from .Routes.Admin.user_edition import *
from .Routes.Admin.user_administration import *
from .Routes.Admin.create_user_admin import *
from .Routes.Admin.profile_admin import *
from .Routes.Admin.ticket_registration_Admin import *
from .Routes.Admin.ticket_details import *
from .Routes.Admin.ticket_update_Admin import *
from .Routes.Admin.ticket_details import *

from .Routes.Agent.help_desk_routes import *
from .Routes.Agent.profile_agent import *
from .Routes.Agent.ticket_details import *
from .Routes.Agent.self_assign_ticket import *
from .Routes.Agent.solve_ticket import *

from .Routes.Client.ticket_registration_user import *
from .Routes.Client.dashboard_user import *
from .Routes.Client.profile_user import *
from .Routes.Client.ticket_details import *
from .Routes.Client.rate_service import *

from .Routes.General.auth import *
from .Routes.General.Functions.chat import *
from .Routes.General.confirm_email import *
from .Routes.General.recover import *
from .Routes.General.home import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
