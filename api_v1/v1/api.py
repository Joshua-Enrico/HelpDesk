#!/usr/bin/python3
""" api aplication """
from web_flask.models.Class import *
from .endpoints import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
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
    port = '5001'
    app.run(host='0.0.0.0', port=port, threaded=True, debug=True)