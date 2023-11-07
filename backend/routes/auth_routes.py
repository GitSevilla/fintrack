from flask import Blueprint, redirect, url_for, session, jsonify
from flask import current_app as app
from extensions import oauth
import secrets

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login')
def login():
    # Redirect to the OAuth provider's login page
    nonce = secrets.token_hex(16)
    session['nonce'] = nonce
    redirect_uri = url_for('auth.callback', _external=True)
    return oauth.auth0.authorize_redirect(redirect_uri=redirect_uri, nonce=nonce)

@auth_bp.route('/callback')
def callback():
    # Handle the response from the OAuth provider
    token = oauth.auth0.authorize_access_token()

    nonce = session.get('nonce')

    user_info = oauth.auth0.parse_id_token(token, nonce=nonce)
    if user_info.get('nonce') != session.pop('nonce', None):
        return 'Nonce mismatched', 401
    
    # Store the user information in, for example, the session
    session['user'] = user_info
    return redirect('/')

@auth_bp.route('/logout')
def logout():
    # Clear the user information from the session
    session.pop('user', None)
    
    # Redirect to the logout URL provided by the OAuth provider
    domain = app.config['AUTH0_DOMAIN']
    client_id = app.config['AUTH0_CLIENT_ID']
    return_to = url_for('auth.home', _external=True)  # Adjust to your home route
    logout_url = f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}'
    return redirect(logout_url)

@auth_bp.route('/')
def home():
    return jsonify(message='Welcome to the Auth0 protected home page')




