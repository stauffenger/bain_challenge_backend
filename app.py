import os
from http import HTTPStatus

from flask_cors import CORS
from flask_restful import Api
from flask import Flask, jsonify
from dotenv import load_dotenv, find_dotenv

from utils import log
from controllers import locations

load_dotenv(find_dotenv())
CORS_ORIGIN = os.getenv("CORS_ORIGIN")
API_HOST = os.getenv("API_HOST")
API_PORT = os.getenv("API_PORT")

app = Flask(__name__) 
api = Api(app)
api.app.config['RESTFUL_JSON'] = {"ensure_ascii": False}
cors = CORS(app, origins=CORS_ORIGIN)

api.add_resource(locations.History, '/locations/history')
api.add_resource(locations.Distance, '/locations/calculateDistance')

@app.route('/healthCheck', methods=['GET']) 
def health_check():   
    health = {
        "message": "The server is running..."
    }
    log.write(f"HEALTH CHECK RESPONSE: {health}")
    return jsonify(health), HTTPStatus.OK

@app.route('/<path:string>', methods=['POST', 'GET', 'PATCH', 'DELETE']) 
def default_message_for_wrong_paths(string): 
    return jsonify({ "message": "Forbidden" }), HTTPStatus.FORBIDDEN

if __name__ == '__main__':
    log.write(f"Starting the server on: {API_HOST}:{API_PORT}...")
    app.run(host=API_HOST, port=API_PORT, debug=True)