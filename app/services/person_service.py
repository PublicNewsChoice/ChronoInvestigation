from app.database import db
from app.models import Person

def get_all_persons():
    return Person.query.all()

def get_person_by_id(id):
    return Person.query.get(id)

def create_person(person_data):
    new_person = Person(**person_data)
    db.session.add(new_person)
    db.session.commit()
    return new_person

def update_person(id, person_data):
    person = Person.query.get(id)
    if person:
        for key, value in person_data.items():
            setattr(person, key, value)
        db.session.commit()
        return person
    return None

def delete_person(id):
    person = Person.query.get(id)
    if person:
        db.session.delete(person)
        db.session.commit()
        return person
    return None