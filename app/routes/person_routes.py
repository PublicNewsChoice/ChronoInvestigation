from flask import render_template, request, redirect, url_for
from app import app, db
from app.models.person import Person

@app.route('/person')
def person_list():
    persons = Person.query.all()
    return render_template('person/list.html', persons=persons)

@app.route('/person/<int:id>')
def person_detail(id):
    person = Person.query.get_or_404(id)
    return render_template('person/detail.html', person=person)

@app.route('/person/create', methods=['GET', 'POST'])
def person_create():
    if request.method == 'POST':
        # Logic for creating a new person entry
        pass
    return render_template('person/create.html')

@app.route('/person/<int:id>/edit', methods=['GET', 'POST'])
def person_edit(id):
    person = Person.query.get_or_404(id)
    if request.method == 'POST':
        # Logic for editing an existing person entry
        pass
    return render_template('person/edit.html', person=person)

@app.route('/person/<int:id>/delete', methods=['GET', 'POST'])
def person_delete(id):
    person = Person.query.get_or_404(id)
    if request.method == 'POST':
        # Logic for deleting a person entry
        pass
    return render_template('person/delete.html', person=person)
