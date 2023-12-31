from __future__ import annotations
from app.repository.mysql import MySqlRepository
from app.model.mysql.User import UserModel, FavouriteCarModel
from app.model.mysql.Car import CarModel
from app.model.mysql import db


class UserController:
    @staticmethod
    def get(id_: int):
        repo = MySqlRepository(db.SessionLocal())
        return repo.get(UserModel, id_)

    @staticmethod
    def all():
        repo = MySqlRepository(db.SessionLocal())
        return repo.all(UserModel)

    @staticmethod
    def filter(*args, **kwargs):
        repo = MySqlRepository(db.SessionLocal())
        return repo.filter(UserModel, *args, **kwargs)

    @staticmethod
    def create(data: dict | list[dict]):
        repo = MySqlRepository(db.SessionLocal())
        data = data if isinstance(data, list) else [data]
        return repo.create([UserModel(**user) for user in data])

    @staticmethod
    def update(id_: int, **kwargs):
        repo = MySqlRepository(db.SessionLocal())
        user = repo.get(UserModel, id_)
        if not user:
            return None
        user.update(**kwargs)
        return repo.update(user)

    @staticmethod
    def delete(id_: int):
        repo = MySqlRepository(db.SessionLocal())
        user = repo.get(UserModel, id_)
        if not user:
            return None
        return repo.delete(user)

    @staticmethod
    def assign_car(id_: int, car_ids: int | list[int]):
        if isinstance(car_ids, int):
            car_ids = [car_ids]
        repo = MySqlRepository(db.SessionLocal())
        cars = UserController.get_cars(id_)
        current_car_ids = [car.id for car in cars if car.id]
        #! We are not checking if the car exist to avoid performance issues
        return repo.create(
            [
                FavouriteCarModel(user_id=id_, car_id=car_id)
                for car_id in car_ids
                if car_id not in current_car_ids
            ]
        )

    @staticmethod
    def unassign_car(id_: int, car_ids: int | list[int]):
        if isinstance(car_ids, int):
            car_ids = [car_ids]
        repo = MySqlRepository(db.SessionLocal())
        for car_id in car_ids:
            instance = repo.filter(
                FavouriteCarModel,
                FavouriteCarModel.user_id == id_,
                FavouriteCarModel.car_id == car_id,
            )
            if not instance:
                continue
            instance = instance[0]
            repo.delete(instance)

    @staticmethod
    def get_cars(id_: int):
        with db.SessionLocal() as session:
            return (
                session.query(CarModel)
                .join(FavouriteCarModel)
                .filter(FavouriteCarModel.user_id == id_)
                .all()
            )
