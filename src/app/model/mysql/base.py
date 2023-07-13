from app.model.mysql import db


class BaseModel(db.Base):
    __abstract__ = True

    def to_dict(self):
        data = {col.name: getattr(self, col.name) for col in self.__table__.columns}
        for relationship in self.__mapper__.relationships:
            if relationship.lazy:  # This mapping should be improved
                continue
            related_data = getattr(self, relationship.key)
            if relationship.uselist:
                data[relationship.key] = [obj.to_dict() for obj in related_data]
        return data

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.__table__.columns:
                setattr(self, key, value)
        return self
