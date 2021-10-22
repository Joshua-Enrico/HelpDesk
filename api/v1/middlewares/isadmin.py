#!/usr/bin/python3
from functools import wraps
from flask import request, g


def isadmin(fn):
    @wraps(fn)
    def decorated_func(*args, **kwargs):
        user = request.environ.get('user')
        if user.get('Rol') != 'Administrador':
            return Response('Unauthorized', mimetype='text/plain', status=403)

        return fn(*args, **kwargs)

    return decorated_func
