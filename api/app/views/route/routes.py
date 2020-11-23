from . import bp
from app.core.helpers import login_required
from app.core.database.models import Route
from flask import request, jsonify
import jwt
from app.core.config import Config
from app.core.serializers import RouteSchema
from app.core.database.db import db_session


@bp.route('/api/v1/routes/', methods=['GET'])
def show_all_routes():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return jsonify({"success": False})
    else:
        access_token = auth_header.split(" ")[1]

    try:
        payload = jwt.decode(
            access_token,
            Config.SECRET_KEY,
            algoritms=['HS256']
        )
    except Exception as err:
        return jsonify({"success": False})

    routes = Route.query.all()
    print(routes)
    response = {
        "routes": RouteSchema().dump(routes),
        "success": True
    }
    return jsonify(response)


@bp.route('/api/v1/route/', methods=['POST'])
def create_route():
    route = Route(user_id=1)

    db_session.add(route)
    db_session.commit()

    response = {
        route: RouteSchema().dump(route)
    }
    return jsonify(response), 201
