#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/endpoints')

from api_v1.v1.endpoints.users import *