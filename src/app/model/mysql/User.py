import sqlalchemy as sa
from app.model.mysql.base import BaseModel


class UserModel(BaseModel):
    __tablename__ = "user"

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.String(255), nullable=False)
    email = sa.Column(sa.String(255), nullable=False)


class FavouriteCarModel(BaseModel):
    __tablename__ = "favourite_car"

    def __init__(self, user_id: int, car_id: int):
        self.user_id = user_id
        self.car_id = car_id

    user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"), primary_key=True)
    car_id = sa.Column(sa.Integer, sa.ForeignKey("car.id"), primary_key=True)
