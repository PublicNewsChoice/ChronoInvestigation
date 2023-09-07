from app.database import db
from app.models import Event

def get_all_events():
    return event.query.all()

def get_event_by_id(id):
    return event.query.get(id)

def create_event(event_data):
    new_event = event(**event_data)
    db.session.add(new_event)
    db.session.commit()
    return new_event

def update_event(id, event_data):
    event = event_data.query.get(id)
    if event:
        for key, value in event_data.items():
            setattr(event, key, value)
        db.session.commit()
        return event
    return None

def delete_event(id):
    event = Event.query.get(id)
    if event:
        db.session.delete(event)
        db.session.commit()
        return event
    return None
