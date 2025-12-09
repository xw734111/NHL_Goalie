from flask import Blueprint, jsonify
from backend.services.nhl_api import fetch_goalie_stats

api = Blueprint('api', __name__)

@api.route('/goalies', methods=['GET'])
def get_goalies():
    goalies = fetch_goalie_stats()
    return jsonify(goalies)