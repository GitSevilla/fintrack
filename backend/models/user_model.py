from extensions import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    oauth_provider = db.Column(db.String(120))
    oauth_id = db.Column(db.String(200), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    name = db.Column(db.String(120))
    created_at = db.Column(db.Datetime, default=datetime.utcnow)
    updated_at = db.Column(db.Datetime, default=datetime.utcnow)

    def lower_case(email):
        return email.lower() if email else None
    
    def save(self):
        self.email = User.lower_case(self.email)
        db.session.add(self)
        db.session.commit()
