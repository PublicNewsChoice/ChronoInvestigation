from datetime import datetime
from app.database import db


class Person(db.Model):
    __tablename__ = 'person'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    date_of_birth = db.Column(db.Date, nullable=True)

    # Foreign keys and relations can be added here based on your database structure
    # For instance, if a person is linked to an organization, you would add:
    # organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=True)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # add other fields that you find necessary for the Person model

    def __repr__(self):
        return f'<Person {self.first_name} {self.last_name}>'
