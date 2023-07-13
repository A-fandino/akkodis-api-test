from __future__ import annotations
from app.repository.mysql import MySqlRepository
from app.model.mysql.Car import CarModel
from app.model.mysql import db


class CarController:
    @staticmethod
    def get(id_: int):
        repo = MySqlRepository(db.SessionLocal())
        return repo.get(CarModel, id_)

    @staticmethod
    def all():
        repo = MySqlRepository(db.SessionLocal())
        return repo.all(CarModel)

    @staticmethod
    def filter(*args, **kwargs):
        repo = MySqlRepository(db.SessionLocal())
        return repo.filter(CarModel, *args, **kwargs)

    @staticmethod
    def create(data: dict | list[dict]):
        repo = MySqlRepository(db.SessionLocal())
        data = data if isinstance(data, list) else [data]
        return repo.create([CarModel(**car) for car in data])

    @staticmethod
    def update(id_: int, **kwargs):
        repo = MySqlRepository(db.SessionLocal())
        car = repo.get(CarModel, id_)
        if not car:
            return None
        car.update(**kwargs)
        return repo.update(car)

    @staticmethod
    def delete(id_: int):
        repo = MySqlRepository(db.SessionLocal())
        car = repo.get(CarModel, id_)
        if not car:
            return None
        return repo.delete(car)
