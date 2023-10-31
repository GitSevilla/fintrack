from flask import Flask
from flask_migrate import Migrate


app = Flask(__name__)

db = app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
migrate = Migrate(app, db)


@app.route('/')
def hello_world():
    return 'Hello, World!'
