"""
flask webapp, registered as a consul client
"""

from flask import Flask, jsonify
import logging
from consulclient import register, deregister
import os

PORT = 8000

# Flask Application
API_V1 = '/api/v1/'
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__, static_url_path='')

register(PORT, None, "webapp")

@app.route(API_V1 + "health", methods=['GET'])
def health():
    """
    health
    """
    return jsonify(health=True)

@app.route("/")
def index():
    """
    hello world
    """
    return 'Hello World! 1.0'

@app.errorhandler(Exception)
def handle_generic_error(err):
    """
    default exception handler
    """
    return 'error: ' + str(err), 500

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', debug=True, threaded=True, port=PORT)
    finally:
        deregister()
        logging.warn('shutting down')
