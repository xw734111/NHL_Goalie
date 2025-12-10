from flask import Flask, jsonify
from flask_cors import CORS
from api import api

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Root endpoint for testing
    @app.route('/')
    def index():
        return jsonify({'message': 'NHL Goalie API', 'version': '1.0'}), 200
    
    app.register_blueprint(api, url_prefix='/api')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5001)  # Changed from 5000 to 5001