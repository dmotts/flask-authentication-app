import logging
import os
from flask import Flask, session, redirect, url_for
from models import db

class AuthApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = os.environ.get('SECRET_KEY', 'your_secret_key')

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db.init_app(self.app)

        # Create the database file if it does not exist
        with self.app.app_context():
            if not os.path.exists('users.db'):
                db.create_all()

        self._setup_routes()

    def _setup_routes(self):
        from auth_routes import AuthRoutes
        auth_routes = AuthRoutes()
        self.app.register_blueprint(auth_routes.blueprint)

        self.app.add_url_rule('/', 'index', self.index)

    def index(self):
        # Redirect to login if user is not authenticated
        if 'username' not in session:
            return redirect(url_for('auth.login'))
        return f"Hello, {session['username']}! You are logged in."

    def run(self):
        self.app.run(debug=True)

app = AuthApp().app

if __name__ == '__main__':
    auth_app = AuthApp()
    auth_app.run()
