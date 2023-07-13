from flask import Blueprint, request
from app.controller.car import CarController
from app.utils.serialize import to_dict
import json

car_bp = Blueprint("car", __name__)


@car_bp.route("/", methods=["GET"])
def get_all_cars():
    return to_dict(CarController.all())


@car_bp.route("/<int:id_>/", methods=["GET"])
def get_car(id_: int):
    car = CarController.get(id_)
    if not car:
        return json.dumps({"error": "Car not found"}), 404
    return to_dict(car)


@car_bp.route("/", methods=["POST"])
def create_car():
    cars = request.get_json()
    if not isinstance(cars, list):
        cars = [cars]
    cars = CarController.create(cars)
    return to_dict(cars), 201


@car_bp.route("/<int:id_>/", methods=["PATCH"])
def update_car(id_: int):
    car_data = request.get_json()
    car = CarController.update(id_, **car_data)
    if not car:
        return json.dumps({"error": "Car not found"}), 404
    return to_dict(car)


@car_bp.route("/<int:id_>/", methods=["DELETE"])
def delete_car(id_: int):
    car = CarController.delete(id_)
    if not car:
        return json.dumps({"error": "Car not found"}), 404
    return to_dict(car)
