from app.core.database.models import User, Route
from .extensions import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


class RouteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Route
