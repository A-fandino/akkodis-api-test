import sqlalchemy as sa
from app.model.mysql.base import BaseModel


class CarModel(BaseModel):
    __tablename__ = "car"

    def __init__(self, name: str, brand: str):
        self.name = name
        self.brand = brand

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.String(255), nullable=False)
    brand = sa.Column(sa.String(255), nullable=False)
