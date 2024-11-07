from http import HTTPStatus

from flask import request
from flask_restful import Resource

from utils import log
from services.locations import history

def get_history():
    response = None
    try:
        locations_history = history.get()
        return locations_history, HTTPStatus.OK
    except Exception as error:
        log.error(error)
        response = {
            "message": "Server internal error."
        }
        return response, HTTPStatus.INTERNAL_SERVER_ERROR

class History(Resource):
    def post(self): 
        response = {
            "message": "Forbidden"
        }
        return response, HTTPStatus.FORBIDDEN
    
    def get(self): 
        log.write(f"REQUEST: {request}")

        response = None
        status = None
        response, status = get_history()
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