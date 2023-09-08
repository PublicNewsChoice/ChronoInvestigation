from flask import render_template, Blueprint, request, redirect, url_for
from app.models import Organization, Person, Event, Action, Timeline
from app.database import db

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('index.html', title='Home')

@main.route('/about')
def about():
    return render_template('about.html', title='About')

@main.route('/organizations')
def organizations():
    organizations = Organization.query.all()
    return render_template('organizations.html', title='Organizations', organizations=organizations)

@main.route('/people')
def people():
    people = Person.query.all()
    return render_template('people.html', title='People', people=people)

@main.route('/events')
def events():
    events = Event.query.all()
    return render_template('events.html', title='Events', events=events)

@main.route('/actions')
def actions():
    actions = Action.query.all()
    return render_template('actions.html', title='Actions', actions=actions)

@main.route('/timelines')
def timelines():
    timelines = Timeline.query.all()
    return render_template('timelines.html', title='Timelines', timelines=timelines)

# Routes for the creation pages
@main.route('/organization/create', methods=['GET', 'POST'])
def create_organization():
    if request.method == 'POST':
        # handle organization creation
        return redirect(url_for('main.organizations'))
    return render_template('create_organization.html', title='Create Organization')

# (Similar routes for creating people, events, actions, and timelines would follow here)

# New route for timeline creator
@main.route('/timeline_creator')
def timeline_creator():
    return render_template('timeline_creator/index.html', title='Timeline Creator')

# New route for timeline linking
@main.route('/timeline_linking')
def timeline_linking():
    return render_template('timeline_linking/index.html', title='Timeline Linking')

# New route for interactive visualization
@main.route('/interactive_visualization')
def interactive_visualization():
    return render_template('interactive_visualization/index.html', title='Interactive Visualization')

# Additional routes for handling updates and deletions might also be necessary

