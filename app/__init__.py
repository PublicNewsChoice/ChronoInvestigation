from flask import Flask
from app.database import db
from app.routes import main_routes, organization_routes, person_routes, event_routes, action_routes

# Initialize the app and the database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ChronoDB'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chronodb.db'
db.init_app(app)

# Importing the models after initializing the database
from app.models import Organization, Event, Person, Action

# Importing the forms after creating the app
from app.forms import OrganizationForm, EventForm, PersonForm, ActionForm

# Register the blueprints for all your routes
app.register_blueprint(main_routes.main)

# In your __init__.py file
app.register_blueprint(organization_routes.organization)

app.register_blueprint(person_routes.person_bp)
app.register_blueprint(event_routes.events)  # update this based on the new name of your blueprint in event_routes.py
app.register_blueprint(action_routes.actions)  # update this based on the new name of your blueprint in action_routes.py


# Now, import your services (if they are being used in your routes)
from app.services import event_service, action_service, organization_service, person_service

@app.before_first_request
def create_tables():
    db.create_all()

# At this point, all your routes and services have been imported and registered, and you can start your application from run.py