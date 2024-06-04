from flask import Flask
from app.routes.users import users_bp
from app.routes.scans import scans_bp
from app.routes.assets import assets_bp
from app.routes.vulnerabilities import vulnerabilities_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(users_bp)
    app.register_blueprint(scans_bp)
    app.register_blueprint(assets_bp)
    app.register_blueprint(vulnerabilities_bp)
    return app