from app.model.mysql import db


class BaseModel(db.Base):
    __abstract__ = True

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.__table__.columns:
                setattr(self, key, value)
        return self
