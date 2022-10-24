#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """Return status of the API"""
    return jsonify({"status": "OK"})
