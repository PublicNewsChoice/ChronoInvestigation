from datetime import datetime
from app.database import db


class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    address = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True, unique=True)  # New field
    phone = db.Column(db.String(20), nullable=True, unique=True)   # New field
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships and foreign keys
    # Here you can add any relationships and foreign keys according to your database design

    def __repr__(self):
        return f'<Organization {self.name}>'

    # New method to get organization by ID
    @classmethod
    def get_by_id(cls, id_):
        return cls.query.filter_by(id=id_).first()

    # New method to get all organizations
    @classmethod
    def get_all(cls):
        return cls.query.all()
