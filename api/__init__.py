from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) # Load configuration
    from api.routes.collect_data import api_blueprint  # Import routes
    app.register_blueprint(api_blueprint)  # Register blueprint
    return app
