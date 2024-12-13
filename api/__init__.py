from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) # load configuration

    from api.routes.update_data import update_data_blueprint  # import routes
    from api.routes.make_trade import make_trade_blueprint

    app.register_blueprint(make_trade_blueprint)  # register blueprints
    app.register_blueprint(update_data_blueprint) 
    return app
