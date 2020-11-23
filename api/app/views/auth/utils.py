import datetime
import jwt
from app.core.config import Config


def generate_access_token(user):

    access_token_payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=10),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload,
                              Config.SECRET_KEY, algorithm='HS256').decode('utf-8')
    return access_token
