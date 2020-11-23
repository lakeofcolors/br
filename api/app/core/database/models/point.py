from sqlalchemy import Column, Integer, String, Enum, Float, ForeignKey
from app.core.database.db import Base
from app.core.database.models.enums import PointType
from sqlalchemy.orm import relationship


class Point(Base):
    __tablename__ = 'points'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), unique=False)
    x = Column(Float, unique=False, nullable=False)
    y = Column(Float, unique=False, nullable=False)
    type = Column(Enum(PointType), default=PointType.default, nullable=False)
    route_id = Column(Integer, ForeignKey('routes.id'))

    def __str__(self):
        return "<Point %r>" % self.name

    def __repr__(self):
        return "<Point %r>" % self.name
