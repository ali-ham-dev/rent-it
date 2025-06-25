import os
from uuid import uuid4
from http import HTTPStatus

from flask import Flask, current_app, redirect, request

from rent_it_api.config import DevelopmentConfig, MigrationConfig, TestingConfig, ProductionConfig

CONFIG_MAP = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "migration": MigrationConfig,
    "production": ProductionConfig
}

# def setup_jwt_manager(app: Flask, jwt_manager: JwtManager):
#     pass

def create_app(environment: str = os.getenv("DEVELOPMENT_ENV", "production"), **kwards): 
    app = Flask(__name__)
    app.config.from_object(CONFIG_MAP.get(environment, ProductionConfig))

    # TODO:
        # DB init.
        # App logging.
        # Migration? 
        # Register blueprints (we'll create these later)
        # from rent_it_api_v1.resources import internal_bp, ops_bp, v1_bp
        # app.register_blueprint(internal_bp)
        # app.register_blueprint(ops_bp)
        # app.register_blueprint(v1_bp)

    @app.route("/")
    def be_nice_swagger_redirect():
        return redirect("/api/v1", code=HTTPStatus.MOVED_PERMANENTLY)
    
    @app.before_request
    def add_logger_context():
        pass

    @app.after_request
    def add_version(response):
        pass

    register_shellcontext(app)

    return app

def register_shellcontext(app: Flask):
    """Register shell context object."""
    def shell_context():
        """Shell context objects."""
        return {
            "app": app,
        }
    
    app.shell_context_processor(shell_context)