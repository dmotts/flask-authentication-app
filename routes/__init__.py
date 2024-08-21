# routes/__init__.py

from .auth_routes import AuthRoutes

def init_app(app):
    auth_routes = AuthRoutes()
    app.register_blueprint(auth_routes.blueprint)
