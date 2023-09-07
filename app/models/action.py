from datetime import datetime
from app import db


class Action(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships and foreign keys
    # Here you would add any relationships and foreign keys according to your database design

    def __repr__(self):
        return f'<Action {self.description}>'
