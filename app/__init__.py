from flask import Flask
from app.routes import main
from app.errors import errors
from app.config import Config
import logging

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # # Force debug mode
    app.debug = app.config["DEBUG"]  

    # Set up logging
    logging.basicConfig(
        level=app.config["LOGGING_LEVEL"],
        # format="%(asctime)s - %(levelname)s - %(message)s" 
        format='[%(asctime)s] in %(filename)s:%(lineno)d %(levelname)s: %(message)s '
    )
    app.logger.info("Microblog startup")


    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

