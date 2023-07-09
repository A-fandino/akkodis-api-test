from app.model.mysql import db
import sqlalchemy as sa


class UserModel(db.Base):
    __tablename__ = "user"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.String(255), nullable=False)
    email = sa.Column(sa.String(255), nullable=False)


class FavouriteCarModel(db.Base):
    __tablename__ = "favourite_car"

    user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"), primary_key=True)
    car_id = sa.Column(sa.Integer, sa.ForeignKey("car.id"), primary_key=True)
