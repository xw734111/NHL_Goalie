import os

class Config:
    DEBUG = os.getenv('FLASK_DEBUG', 'false') == 'true'
    TESTING = os.getenv('FLASK_TESTING', 'false') == 'true'
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    API_URL = "https://api.nhle.com/stats/rest/en/goalie/summary"
    USER_AGENT = "Chrome/138.0"