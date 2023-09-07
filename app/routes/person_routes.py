from flask import render_template, url_for, flash, redirect, request, Blueprint
from app.database import db
from app.models import Person
from app.forms import PersonForm

main_bp = Blueprint('main', __name__)
person_bp = Blueprint('person', __name__)

@person_bp.route('/person/new', methods=['GET', 'POST'])
def new_person():
    form = PersonForm()
    if form.validate_on_submit():
        person = Person(name=form.name.data, email=form.email.data, organization_id=form.organization_id.data)
        db.session.add(person)
        db.session.commit()
        flash('A new person has been created!', 'success')
        return redirect(url_for('person.people'))
    return render_template('person/create.html', title='New Person', form=form, legend='New Person')

@person_bp.route('/person/<int:person_id>')
def person_details(person_id):
    person = Person.query.get_or_404(person_id)
    return render_template('person/detail.html', title=person.name, person=person)

@person_bp.route('/person/<int:person_id>/update', methods=['GET', 'POST'])
def update_person(person_id):
    person = Person.query.get_or_404(person_id)
    form = PersonForm()
    if form.validate_on_submit():
        person.name = form.name.data
        person.email = form.email.data
        person.organization_id = form.organization_id.data
        db.session.commit()
        flash('The person information has been updated!', 'success')
        return redirect(url_for('person.person_details', person_id=person.id))
    elif request.method == 'GET':
        form.name.data = person.name
        form.email.data = person.email
        form.organization_id.data = person.organization_id
    return render_template('person/edit.html', title='Update Person', form=form, legend='Update Person')

@person_bp.route('/person/<int:person_id>/delete', methods=['POST'])
def delete_person(person_id):
    person = Person.query.get_or_404(person_id)
    db.session.delete(person)
    db.session.commit()
    flash('The person has been deleted!', 'success')
    return redirect(url_for('person.people'))

@person_bp.route('/people')
def people():
    people = Person.query.all()
    return render_template('person/list.html', people=people)
