from __future__ import annotations
from app.model.mysql.base import BaseModel


def to_dict(instance: BaseModel) -> dict | list[dict] | None:
    if isinstance(instance, list):
        return [to_dict(i) for i in instance]
    if isinstance(instance, BaseModel):
        return instance.to_dict()
    return None
