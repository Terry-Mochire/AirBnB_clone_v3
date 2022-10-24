#!/usr/bin/python3
""" Index script """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """ Returns status of the application """
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """ Returns stats of objects """
    return jsonify({
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    })
