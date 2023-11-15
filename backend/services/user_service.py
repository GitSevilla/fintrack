from models.user_model import User
from extensions import db

def verify_user_by_id(oauth_id):
    user = User.query.filter_by(oauth_id=oauth_id).first()

    return user

def create_user(oauth_id, email, name):
    new_user = User(
        oauth_id=oauth_id,
        email=email,
        name=name
    )
    db.session.add(new_user)
    db.session.commit()

    return new_user

def delete_user(oauth_id):
    user = verify_user_by_id(oauth_id)

    if user is not None:
        db.session.delete(user)
        db.session.commit()
        return user
    else:
        #Placeholder
        print("User not found")