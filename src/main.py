from flask import Flask, Blueprint, request, render_template
from app.routes.user import user_bp
from app.routes.car import car_bp
import logging
from app.udp.server import udp_server
import threading

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler("app.log")
fh.setFormatter(
    logging.Formatter("%(asctime)s - %(message)s")
)  # I am using default timestamp as it is easier to read. Was a unix timestamp required?
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


def create_app():
    app = Flask(__name__)
    api_bp = Blueprint("api", __name__, url_prefix="/api")

    # Entity Blueprints
    api_bp.register_blueprint(user_bp, url_prefix="/user")
    api_bp.register_blueprint(car_bp, url_prefix="/car")
    ###################

    app.register_blueprint(api_bp)

    @app.route("/ui/")
    def ui():
        return render_template("swaggerui.html")

    @app.before_request
    def log_request_info():
        info = {
            "url": request.url,
            "method": request.method,
            "data": request.data,
        }

        def log_request():
            logger.info(
                f"URL: {info['url']} | Method: {info['method']} | Data: {info['data']}"
            )

        thread = threading.Thread(target=log_request)
        thread.start()

    return app


if __name__ == "__main__":
    server_thread = threading.Thread(target=udp_server)
    server_thread.start()
    app = create_app()
    app.run()
