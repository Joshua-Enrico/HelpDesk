#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/endpoints')

from api.v1.endpoints.users import *
from api.v1.endpoints.tickets import *
from api.v1.endpoints.user_summary import *
from api.v1.endpoints.user_profile_admin import *