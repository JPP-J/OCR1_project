import os
import logging

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # DEBUG = os.environ.get('FLASK_DEBUG', '0') == '1'
    # Convert FLASK_DEBUG to an integer first, then to a boolean
    DEBUG = bool(int(os.environ.get('FLASK_DEBUG', 0)))
    

    # Logging Configuration
    LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO

