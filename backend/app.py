from flask import Flask, redirect, render_template, session, url_for
from os import environ as env
from extensions import db, migrate, oauth
from routes.main_routes import main
from routes.income_routes import income_bp
from routes.expense_routes import expense_bp

def create_app():

    app = Flask(__name__)
    app.secret_key = env.get("APP_SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    #Database config
    db.init_app(app)
    app.register_blueprint(main)
    app.register_blueprint(income_bp)
    app.register_blueprint(expense_bp)
    migrate.init_app(app, db)

    #OAuth config
    oauth.init_app(app)
    oauth.register(
        "auth0",
        client_id = env.get("AUTH0_CLIENT_ID"),
        client_secret = env.get("AUTH0_CLIENT_SECRET"),
        client_kwargs = {
            "scope": "openid profile email",
        },
        server_metadata_url = f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
    )

    
    
    return app

app = create_app()