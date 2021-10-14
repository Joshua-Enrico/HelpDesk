#!/usr/bin/python3
from .models import app
from .routes.admin import *
from .routes.admin_user import *
from .routes.auth import *
from .routes.confirm_email import *
from .routes.dashboard import *
from .routes.home import *
from .routes.recover import *
from .routes.registra_ticket import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
