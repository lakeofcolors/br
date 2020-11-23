from functools import wraps


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)

        return f(*args, **kwargs)
    return wrapper
