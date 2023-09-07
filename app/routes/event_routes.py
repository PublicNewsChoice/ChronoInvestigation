from flask import render_template, url_for, flash, redirect, request, Blueprint
from app.database import db
from app.models import Event
from app.forms import EventForm

main_bp = Blueprint('main', __name__)
events = Blueprint('events', __name__)
person_bp = Blueprint('person', __name__)

# Create
@events.route('/event/create', methods=['GET', 'POST'])
def create_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(
            name=form.name.data,
            description=form.description.data,
            # ... include other fields
        )
        db.session.add(event)
        db.session.commit()
        flash('Event created successfully!', 'success')
        return redirect(url_for('events.list_events'))
    return render_template('event/create.html', title='Create Event', form=form)

# Read
@events.route('/event/<int:id>', methods=['GET'])
def event_detail(id):
    event = Event.query.get_or_404(id)
    return render_template('event/detail.html', title='Event Details', event=event)

# Update
@events.route('/event/<int:id>/update', methods=['GET', 'POST'])
def update_event(id):
    event = Event.query.get_or_404(id)
    form = EventForm()
    if form.validate_on_submit():
        event.name = form.name.data
        event.description = form.description.data
        # ... update other fields
        db.session.commit()
        flash('Event updated successfully!', 'success')
        return redirect(url_for('events.event_detail', id=event.id))
    elif request.method == 'GET':
        form.name.data = event.name
        form.description.data = event.description
        # ... pre-fill other fields
    return render_template('event/edit.html', title='Update Event', form=form, event=event)

# Delete
@events.route('/event/<int:id>/delete', methods=['POST'])
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    flash('Event deleted successfully!', 'success')
    return redirect(url_for('events.list_events'))

# List
@events.route('/events', methods=['GET'])
def list_events():
    events = Event.query.all()
    return render_template('event/list.html', title='Events', events=events)
