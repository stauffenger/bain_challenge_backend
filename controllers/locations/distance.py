import json
from http import HTTPStatus

from flask import request
from flask_restful import Resource

from utils import log
from services.locations import distance

def calculate_distance(source, destination):
    response = None
    try:
        result = distance.calculate_from_a_to_b(source, destination)
        if 'distance_km' in result:
            response = { "km": result['distance_km'] }
            message_status = HTTPStatus.OK
        elif 'not_found' in result:
            response = {
                "message": f"Address not found.",
                "addresses": result['not_found']
            }
            message_status = HTTPStatus.NOT_FOUND
        else:
            response = {
                "message": f"Conflict."
            }
            if 'destination_alternatives' in result:
                response['destination_alternatives'] = result['destination_alternatives']
            
            if 'source_alternatives' in result:
                response['source_alternatives'] = result['source_alternatives']

            message_status = HTTPStatus.CONFLICT
        
        return response, message_status
    except Exception as error:
        log.error(error)
        response = {
            "message": "Server internal error."
        }
        message_status = HTTPStatus.INTERNAL_SERVER_ERROR
        return response, message_status

class Distance(Resource):
    def post(self): 
        response = {
            "message": "Forbidden"
        }
        return response, HTTPStatus.FORBIDDEN
    
    def get(self): 
        source = request.args.get('source')
        destination = request.args.get('destination')
        log.write(f"REQUEST: {request}")

        response = None
        status = None
        if source and destination:
            response, status = calculate_distance(source, destination)
        else:
            response = {
                "message": "Bad Request."
            }
            status = HTTPStatus.BAD_REQUEST

        log.write(f"RESPONSE: {response}")
        return response, status
    
    def patch(self):
        response = {
            "message": "Forbidden"
        }
        return response, HTTPStatus.FORBIDDEN
    
    def delete(self):
        response = {
            "message": "Forbidden"
        }
        return response, HTTPStatus.FORBIDDEN