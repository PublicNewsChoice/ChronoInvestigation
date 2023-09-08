from flask import render_template, Blueprint
from app.models import Organization, Person
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
