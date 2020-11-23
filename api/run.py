from app import create_app
from app.core.config import Config

if __name__ == "__main__":
    create_app(Config)
