from flask import Flask, Blueprint, url_for
from app.routes.user import user_bp
from app.routes.car import car_bp

app = Flask(__name__)
api_bp = Blueprint("api", __name__, url_prefix="/api")

# Entity Blueprints
api_bp.register_blueprint(user_bp, url_prefix="/user")
api_bp.register_blueprint(car_bp, url_prefix="/car")

###################

app.register_blueprint(api_bp)


if __name__ == "__main__":
    app.run(debug=True)
