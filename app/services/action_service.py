from app import db
from app.models import Action

def get_all_actions():
    return Action.query.all()

def get_action_by_id(id):
    return Action.query.get(id)

def create_action(action_data):
    new_action = Action(**action_data)
    db.session.add(new_action)
    db.session.commit()
    return new_action

def update_action(id, action_data):
    action = Action.query.get(id)
    if action:
        for key, value in action_data.items():
            setattr(action, key, value)
        db.session.commit()
        return action
    return None

def delete_action(id):
    action = Action.query.get(id)
    if action:
        db.session.delete(action)
        db.session.commit()
        return action
    return None