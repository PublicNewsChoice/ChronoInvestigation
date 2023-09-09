from datetime import datetime
from app.database import db

# Define association tables for many-to-many relationships
organization_timeline = db.Table('organization_timeline',
                                 db.Column('organization_id', db.Integer, db.ForeignKey('organization.id'), primary_key=True),
                                 db.Column('timeline_id', db.Integer, db.ForeignKey('timeline.id'), primary_key=True)
                                 )

person_timeline = db.Table('person_timeline',
                           db.Column('person_id', db.Integer, db.ForeignKey('person.id'), primary_key=True),
                           db.Column('timeline_id', db.Integer, db.ForeignKey('timeline.id'), primary_key=True)
                           )

event_timeline = db.Table('event_timeline',
                          db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
                          db.Column('timeline_id', db.Integer, db.ForeignKey('timeline.id'), primary_key=True)
                          )

action_timeline = db.Table('action_timeline',
                           db.Column('action_id', db.Integer, db.ForeignKey('action.id'), primary_key=True),
                           db.Column('timeline_id', db.Integer, db.ForeignKey('timeline.id'), primary_key=True)
                           )

class Organization(db.Model):
    __tablename__ = 'organization'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)  # add other fields as necessary
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    timelines = db.relationship('Timeline', secondary=organization_timeline, back_populates='organizations')

class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)  # add other fields as necessary
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    timelines = db.relationship('Timeline', secondary=person_timeline, back_populates='people')

class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)  # add other fields as necessary
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    timelines = db.relationship('Timeline', secondary=event_timeline, back_populates='events')

class Action(db.Model):
    __tablename__ = 'action'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String, nullable=False)  # add other fields as necessary
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    timelines = db.relationship('Timeline', secondary=action_timeline, back_populates='actions')

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)  # add other fields as necessary
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Timeline(db.Model):
    __tablename__ = 'timeline'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)  # add other fields as necessary
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    events = db.relationship('Event', secondary=event_timeline, back_populates='timelines')
    actions = db.relationship('Action', secondary=action_timeline, back_populates='timelines')
    people = db.relationship('Person', secondary=person_timeline, back_populates='timelines')
    organizations = db.relationship('Organization', secondary=organization_timeline, back_populates='timelines')
