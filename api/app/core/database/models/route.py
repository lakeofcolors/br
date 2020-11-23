from sqlalchemy import Column, Integer, String, Enum, Float, ForeignKey
from app.core.database.db import Base
from sqlalchemy.orm import relationship


class Route(Base):
    __tablename__ = 'routes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    points = relationship('Point', backref='route')

    def __str__(self):
        return "<Route %r>" % self.id

    def __repr__(self):
        return "<Route %r>" % self.id
