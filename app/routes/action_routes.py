from flask import render_template, url_for, flash, redirect, request, Blueprint
from app.database import db
from app.models import Action
from app.forms import ActionForm

actions = Blueprint('actions', __name__)

# Create
@actions.route('/action/create', methods=['GET', 'POST'])
def create_action():
    form = ActionForm()
    if form.validate_on_submit():
        # create a new action and add it to the database
        action = Action(name=form.name.data, description=form.description.data)
        db.session.add(action)
        db.session.commit()
        flash('Action created successfully!', 'success')
        return redirect(url_for('actions.list_actions'))
    return render_template('action/create.html', title='Create Action', form=form)

# Read
@actions.route('/action/<int:id>', methods=['GET'])
def action_detail(id):
    # get action details by id
    action = Action.query.get_or_404(id)
    return render_template('action/detail.html', title='Action Details', action=action)

# Update
@actions.route('/action/<int:id>/update', methods=['GET', 'POST'])
def update_action(id):
    action = Action.query.get_or_404(id)
    form = ActionForm()
    if form.validate_on_submit():
        # update the action details
        action.name = form.name.data
        action.description = form.description.data
        db.session.commit()
        flash('Action updated successfully!', 'success')
        return redirect(url_for('actions.action_detail', id=action.id))
    elif request.method == 'GET':
        form.name.data = action.name
        form.description.data = action.description
    return render_template('action/edit.html', title='Update Action', form=form, action=action)

# Delete
@actions.route('/action/<int:id>/delete', methods=['POST'])
def delete_action(id):
    action = Action.query.get_or_404(id)
    db.session.delete(action)
    db.session.commit()
    flash('Action deleted successfully!', 'success')
    return redirect(url_for('actions.list_actions'))

# List
@actions.route('/actions', methods=['GET'])
def list_actions():
    actions = Action.query.all()
    return render_template('action/list.html', title='Actions', actions=actions)
