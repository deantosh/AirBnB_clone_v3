#!/usr/bin/python3
"""
Create a new view for the link between Place objects
and Amenity objects that handles all default RESTFul
API actions
"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.amenity import Amenity
from os import getenv


@app_views.route('/places/<place_id>/amenities', methods=['GET'],
                 strict_slashes=False)
@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['GET', 'DELETE', 'POST'], strict_slashes=False)
def place_amenity_requests(place_id=None, amenity_id=None):
    """Handles API requests for place/amenity relationships"""
    mode = getenv('HBNB_TYPE_STORAGE')

    if request.method == 'GET':
        return handle_get_request(place_id)

    elif request.method == 'DELETE':
        return handle_delete_request(place_id, amenity_id, mode)

    elif request.method == 'POST':
        return handle_post_request(place_id, amenity_id, mode)

    else:
        abort(501)


def handle_get_request(place_id):
    """Handles GET request for place amenities"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    amenity_list = [amenity.to_dict() for amenity in place.amenities]
    return jsonify(amenity_list)


def handle_delete_request(place_id, amenity_id, mode):
    """Handles DELETE request to remove an amenity from a place"""
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)
    if place is None or amenity is None or amenity not in place.amenities:
        abort(404)

    if mode != 'db':
        place.amenity_ids.remove('Amenity.' + amenity_id)

    storage.delete(amenity)
    storage.save()

    return jsonify({}), 200


def handle_post_request(place_id, amenity_id, mode):
    """Handles POST request to link an amenity to a place"""
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)
    if place is None or amenity is None:
        abort(404)

    if amenity in place.amenities:
        return jsonify(amenity.to_dict()), 200

    if mode == 'db':
        place.amenities.append(amenity)
    else:
        place.amenity_ids.append('Amenity.' + amenity_id)

    storage.save()
    return jsonify(amenity.to_dict()), 201
