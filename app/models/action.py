from datetime import datetime
from app.database import db
from app.models.article import Article  # Assuming you have an article.py file in your models directory

# Creating an association table for the many-to-many relationship between actions and articles
action_articles_association = db.Table('action_articles_association',
                                       db.Column('action_id', db.Integer, db.ForeignKey('action.id'), primary_key=True),
                                       db.Column('article_id', db.Integer, db.ForeignKey('article.id'),
                                                 primary_key=True)
                                       )


class Action(db.Model):
    __tablename__ = 'action'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship fields
    articles = db.relationship('Article', secondary=action_articles_association, back_populates='actions')

    # Relationship with timelines
    timelines = db.relationship('Timeline', secondary='action_timeline',
                                back_populates='actions')  # Assuming you have a back_populates field in your Timeline model

# Remember to import this class where you define your Timeline model to avoid circular imports.
