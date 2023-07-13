from flask import Blueprint, request
from app.controller.user import UserController
from app.utils.serialize import to_dict
import json

user_bp = Blueprint("user", __name__)


@user_bp.route("/", methods=["GET"])
def get_all_user():
    return to_dict(UserController.all())


@user_bp.route("/<int:id_>/", methods=["GET"])
def get_user(id_: int):
    user = UserController.get(id_)
    if not user:
        return json.dumps({"error": "User not found"}), 404
    return to_dict(user)


@user_bp.route("/", methods=["POST"])
def create_user():
    users = request.get_json()
    if not isinstance(users, list):
        users = [users]
    users = UserController.create(users)
    return to_dict(users)


@user_bp.route("/<int:id_>/", methods=["PUT"])
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
