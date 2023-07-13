from flask import Blueprint, request
from app.controller.user import UserController
from app.utils.serialize import to_dict
import json
from app.udp.client import udp_client
import threading

user_bp = Blueprint("user", __name__)


@user_bp.route("/", methods=["GET"])
def get_all_user():
    return to_dict(UserController.all())


@user_bp.route("/<int:id_>/", methods=["GET"])
def get_user(id_: int):
    user = UserController.get(id_)
    if not user:
        return json.dumps({"error": "User not found"}), 404
    user_dict = to_dict(user)
    client_thread = threading.Thread(target=udp_client, args=(user_dict,))
    client_thread.start()
    return user_dict


@user_bp.route("/", methods=["POST"])
def create_user():
    users = request.get_json()
    if not isinstance(users, list):
        users = [users]
    users = UserController.create(users)
    return to_dict(users)


@user_bp.route("/<int:id_>/", methods=["PATCH"])
def update_user(id_: int):
    user_data = request.get_json()
    user = UserController.update(id_, **user_data)
    if not user:
        return json.dumps({"error": "User not found"}), 404
    return to_dict(user)


@user_bp.route("/<int:id_>/", methods=["DELETE"])
def delete_user(id_: int):
    user = UserController.delete(id_)
    if not user:
        return json.dumps({"error": "User not found"}), 404
    return to_dict(user)


@user_bp.route("/<int:id_>/cars/", methods=["GET"])
def get_cars(id_: int):
    return to_dict(UserController.get_cars(id_))


@user_bp.route("/<int:id_>/cars/", methods=["POST"])
def assign_car(id_: int):
    body = request.get_json()
    car_ids = body.get("car_ids")
    UserController.assign_car(id_, car_ids)
    return json.dumps({"success": "Cars assigned successfully"})


@user_bp.route("/<int:id_>/cars/<int:car_id>", methods=["DELETE"])
def unassign_car(id_: int, car_id: int):
    UserController.unassign_car(id_, car_id)
    return json.dumps({"success": "Cars unassigned successfully"})
