from __future__ import annotations
from sqlalchemy.orm import Session
from app.model.mysql.base import BaseModel


class MySqlRepository:
    def __init__(self, session: Session):
        self.session = session

    def all(self, Model):
        with self.session as session:
            return session.query(Model).all()

    def get(self, Model, id_):
        with self.session as session:
            return session.query(Model).get(id_)

    def filter(self, Model, *args, **kwargs):
        with self.session as session:
            return session.query(Model).filter(*args, **kwargs).all()

    def create(self, Model, instances: BaseModel | list[BaseModel]):
        if not isinstance(instances, list):
            instances = [instances]
        with self.session as session:
            session.add_all(instances)
            session.commit()
            for inst in instances:
                session.refresh(inst)
            return instances

    def update(self, instance: BaseModel):
        with self.session as session:
            instance = session.merge(instance)
            session.commit()
            session.refresh(instance)
            return instance

    def delete(self, instance):
        with self.session as session:
            session.delete(instance)
            session.commit()
            return instance
