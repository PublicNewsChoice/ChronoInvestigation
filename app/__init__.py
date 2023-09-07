from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the app and the database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ChronoDB'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chronodb.db'
db = SQLAlchemy(app)

# Importing the models after initializing the database
from app.models import Organization, Event, Person, Action  # assuming Action is a model you have created

# Importing the forms after creating the app
from app.forms import OrganizationForm, EventForm, PersonForm, ActionForm  # assuming ActionForm is a form you have created

# Now, import your routes
from app import routes
