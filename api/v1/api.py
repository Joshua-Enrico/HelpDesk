#!/usr/bin/python3
""" api aplication """
from api.v1 import app_views
from api.v1.middlewares.auth import AuthMiddleware
from web_flask.models import db
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Helpdesk:Helpdesk@localhost/HelpDesk'#create database and user
app.register_blueprint(app_views)
app.wsgi_app = AuthMiddleware(app.wsgi_app)

cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

if __name__ == "__main__":
    """ Main Function """
    db.init_app(app)
    port = 5001
    app.run(host='0.0.0.0', port=port, threaded=True, debug=True)
