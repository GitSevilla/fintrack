from flask import Flask
from extensions import db, migrate
from routes.main_routes import main

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    db.init_app(app)
    app.register_blueprint(main)

    from models.income_model import Income
    migrate.init_app(app, db)

    
    
    return app

app = create_app()