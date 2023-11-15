from flask import Blueprint, jsonify



main = Blueprint('main', __name__)

@main.route('/')
def hello_world():
    return 'Hello, World!'

@main.route('/user')
def user_logged_in():
    return jsonify(message='Welcome to the User Homepage')

