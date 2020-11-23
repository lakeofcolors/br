from sqlalchemy import Column, Integer, String
from app.core.database.db import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(256), unique=True)
    password = Column(String(128), unique=False, nullable=False)
    routes = relationship('Route', backref='user')

    def __str__(self):
        return "<User %r>" % self.email

    def __repr__(self):
        return "<User %r>" % self.email
