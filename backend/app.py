from flask import Flask
from extensions import db, migrate
from routes.main_routes import main
from routes.income_routes import income_bp
from routes.expense_routes import expense_bp

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    db.init_app(app)
    app.register_blueprint(main)
    app.register_blueprint(income_bp)
    app.register_blueprint(expense_bp)

    migrate.init_app(app, db)

    
    
    return app

app = create_app()