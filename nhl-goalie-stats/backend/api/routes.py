from flask import jsonify
from . import api

print("Routes module loaded!")

@api.route('/health', methods=['GET'])
def health_check():
    print("Health check called!")
    return jsonify({'status': 'ok', 'message': 'API is running'}), 200

@api.route('/test', methods=['GET'])
def test():
    print("Test endpoint called!")
    return jsonify({'message': 'Test endpoint working'}), 200