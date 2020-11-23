from . import bp
from flask import request, jsonify
from app.core.database.models import User
from app.core.serializers import UserSchema
from .utils import generate_access_token


@bp.route('/api/v1/auth/', methods=['POST'])
def auth():
    data = request.json

    try:
        user = User.query.filter_by(email=data['email']).first_or_404()
        access_token = generate_access_token(user)

    except Exception as err:
        return jsonify({"success": False}), 404

    response = {
        "success": True,
        "user": UserSchema().dump(user),
        "access_token": access_token,
    }
    return jsonify(response), 201
