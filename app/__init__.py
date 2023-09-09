from flask import Flask, render_template
from app.database import db

# Import the blueprints for all your routes
from app.routes import main_routes, organization_routes, person_routes, event_routes, action_routes, resources_routes, article_routes
from app.routes.timeline_creator import timeline_creator_bp
from app.routes.timeline_linking import timeline_linking_bp
from app.routes.interactive_visualization import interactive_visualization_bp

# Initialize the app and the database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ChronoDB'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chronodb.db'
db.init_app(app)

# Register the blueprints for all your routes
app.register_blueprint(main_routes.main)
app.register_blueprint(organization_routes.organization)
app.register_blueprint(person_routes.person_bp)
app.register_blueprint(event_routes.events)
app.register_blueprint(action_routes.action_routes)  # Updated the blueprint registration for action routes
app.register_blueprint(resources_routes.resource_routes, url_prefix='/resources')
app.register_blueprint(article_routes.article_routes, url_prefix='/articles')

# Register the Blueprint with a URL prefix for the timeline features
app.register_blueprint(timeline_creator_bp, url_prefix='/timeline_creator')
app.register_blueprint(timeline_linking_bp, url_prefix='/timeline_linking')
app.register_blueprint(interactive_visualization_bp, url_prefix='/interactive_visualization')

# Now, import your services (if they are being used in your routes)
from app.services import event_service, action_service, organization_service, person_service, article_service

# Importing the models after initializing the database
from app.models import Organization, Event, Person, Action, Article

# Importing the forms after creating the app
from app.forms import OrganizationForm, EventForm, PersonForm, ActionForm, ArticleForm

@app.before_first_request
def create_tables():
    db.create_all()

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

# At this point, all your routes and services have been imported and registered, and you can start your application from run.py