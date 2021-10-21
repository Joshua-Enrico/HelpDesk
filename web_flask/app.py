#!/usr/bin/python3
from .models import app
from .Routes.admin import *
from .Routes.Admin.admin_user import *
from .Routes.General.auth import *
from .Routes.General.confirm_email import *
from .Routes.General.recover import *
from .Routes.dashboard import *
from .Routes.General.home import *
from .Routes.registra_ticket import *
from .Routes.create_user_admin import *
from .Routes.profile import *
from .Routes.Agent.help_desk_routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
