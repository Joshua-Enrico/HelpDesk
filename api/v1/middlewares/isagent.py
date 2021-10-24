#!/usr/bin/python3
from functools import wraps
from flask import request, g
from werkzeug.wrappers import Response


def isagent(fn):
    @wraps(fn)
    def decorated_func(*args, **kwargs):
        user = request.environ.get('user')
        if user.get('Rol') != 'Agente Helpdesk':
            return Response('Unauthorized', mimetype='text/plain', status=403)

        return fn(*args, **kwargs)

    return decorated_func
