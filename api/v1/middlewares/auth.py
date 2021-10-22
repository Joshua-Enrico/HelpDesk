#!/usr/bin/python3
""" This module defines middleware functions to authorize API queries  """
from werkzeug.wrappers import Request, Response, ResponseStream
from flask import request
from api.utils import decode_token


class AuthMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)

        # authorization = request.headers.get('Authorization', 'Bearer')
        # token = authorization.split()[-1]
        # user = decode_token(token)
        # if user is None and request.method != 'OPTIONS':
        #     res = Response('Authorization failed', mimetype= 'text/plain', status=401)
        #     return res(environ, start_response)

        # environ['user'] = user
        environ['user'] = {'Rol': 'Administrador'}
        return self.app(environ, start_response)
