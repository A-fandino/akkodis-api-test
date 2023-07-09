from app.model.mysql import db
import sqlalchemy as sa


class CarModel(db.Base):
    __tablename__ = "car"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.String(255), nullable=False)
    brand = sa.Column(sa.String(255), nullable=False)
