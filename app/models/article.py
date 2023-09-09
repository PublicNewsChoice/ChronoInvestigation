from datetime import datetime
from app.database import db

# Defining many-to-many relationships between Article and Event, and Article and Action
articles_events_association = db.Table(
    'articles_events',
    db.Column('article_id', db.Integer, db.ForeignKey('article.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True)
)

articles_actions_association = db.Table(
    'articles_actions',
    db.Column('article_id', db.Integer, db.ForeignKey('article.id'), primary_key=True),
    db.Column('action_id', db.Integer, db.ForeignKey('action.id'), primary_key=True)
)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False, unique=True, index=True)  # Added unique constraint and index
    url = db.Column(db.String(255), nullable=False, unique=True, index=True)  # Added index
    source = db.Column(db.String(255), nullable=True)
    publication_date = db.Column(db.DateTime, nullable=True, index=True)  # Added index
    summary = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Many-to-many relationships with Action and Event
    events = db.relationship('Event', secondary=articles_events_association, back_populates='articles')
    actions = db.relationship('Action', secondary=articles_actions_association, back_populates='articles')

    def __repr__(self):
        return f'<Article {self.title}>'
