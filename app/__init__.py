from flask import Flask
from app.routes.api import api

def create_app():
    app = Flask(__name__)

    app.register_blueprint(api, url_prefix="/api")

    @app.route("/")
    def home():
        return {"message": "Student Academic Management Platform"}

    @app.route("/api/health")
    def health():
        return {"status": "healthy"}

    return app

