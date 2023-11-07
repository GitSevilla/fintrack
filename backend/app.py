from flask import Flask
from os import environ as env
from extensions import db, migrate, oauth
from routes.main_routes import main
from routes.income_routes import income_bp
from routes.expense_routes import expense_bp
from routes.auth_routes import auth_bp

def create_app():

    app = Flask(__name__)
    app.config['AUTH0_DOMAIN'] = env.get('AUTH0_DOMAIN')
    app.config['AUTH0_CLIENT_ID'] = env.get('AUTH0_CLIENT_ID')
    app.config['AUTH0_CLIENT_SECRET'] = env.get('AUTH0_CLIENT_SECRET')
    app.config['AUTH0_BASE_URL'] = 'https://' + app.config['AUTH0_DOMAIN']
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.secret_key = env.get("APP_SECRET_KEY")

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
    app.register_blueprint(auth_bp)

    
    return app

app = create_app()