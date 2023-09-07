from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Action
from app.forms import ActionForm

@app.route('/actions')
def actions():
    actions = Action.query.all()
    return render_template('action/list.html', actions=actions)

@app.route('/action/create', methods=['GET', 'POST'])
def create_action():
    form = ActionForm()
    if form.validate_on_submit():
        action = Action(
            name=form.name.data,
            # ... include other fields here ...
        )
        db.session.add(action)
        db.session.commit()
        flash('Your action has been created.')
        return redirect(url_for('actions'))
    return render_template('action/create.html', title='Create Action', form=form)

@app.route('/action/<int:id>', methods=['GET', 'POST'])
def edit_action(id):
    action = Action.query.get_or_404(id)
    form = ActionForm(obj=action)
    if form.validate_on_submit():
        form.populate_obj(action)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('actions'))
    return render_template('action/edit.html', title='Edit Action', form=form, action=action)

@app.route('/action/<int:id>/delete', methods=['POST'])
def delete_action(id):
    action = Action.query.get_or_404(id)
    db.session.delete(action)
    db.session.commit()
    flash('Action has been deleted.')
    return redirect(url_for('actions'))
