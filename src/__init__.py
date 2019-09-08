"""Base point for the app."""
from flask import Flask


def create_app():
    """App factory structure."""
    flask_app = Flask(__name__)
    # flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
    # flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # flask_app.app_context().push()
    # db.init_app(flask_app)
    # db.create_all()
    from .navigation import bl_nav    # noqa
    flask_app.register_blueprint(bl_nav)
    # print(flask_app.blueprints)
    return flask_app

app = create_app()


