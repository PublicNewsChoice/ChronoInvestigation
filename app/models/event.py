from datetime import datetime
from app.database import db

# Creating an association table for the many-to-many relationship between events and articles
event_articles_association = db.Table('event_articles_association',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
    db.Column('article_id', db.Integer, db.ForeignKey('article.id'), primary_key=True)
)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    # Other fields ...

    # Setting up the relationship with the Article model
    articles = db.relationship('Article', secondary=event_articles_association, back_populates='events')

    # Rest of your model definitions ...
