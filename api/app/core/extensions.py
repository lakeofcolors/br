from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_admin import Admin

migrate = Migrate()
ma = Marshmallow()
admin = Admin(name='br', template_mode='bootstrap3')


