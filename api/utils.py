#!/usr/bin/python3
""" This module defines util functions for API """
import jwt
from os import getenv
from flask import jsonify
from base64 import b64encode as enc64


def jsonify_pagination(pag_obj):
    """ Creates a pagination dictionary """
    keys = ['has_next', 'has_prev',
            'next_num', 'page', 'pages', 'per_page',
            'prev_num', 'total']
    d = {k: pag_obj.__getattribute__(k) for k in keys}
    d['items'] = [r._asdict() for r in pag_obj.items]
    return jsonify(d)


def generate_token(data):
    """ Generates a jwt token """
    try:
        payload = { 'user': data }
        return jwt.encode(
            payload,
            enc64(getenv('JWT_KEY').encode('utf-8')),
            algorithm='HS256'
        )
    except:
        return None


def decode_token(token):
    """ Decodes a jwt token """
    try:
        return jwt.decode(
            token,
            enc64(getenv('JWT_KEY').encode('utf-8'))
        )
    except:
        return None
