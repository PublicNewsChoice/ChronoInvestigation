from flask import render_template, url_for, flash, redirect, request, Blueprint
from app import db
from app.models import Organization
from app.forms import OrganizationForm

main_bp = Blueprint('main', __name__)
organization = Blueprint('organization', __name__)
person_bp = Blueprint('person', __name__)

@organization.route('/organization/new', methods=['GET', 'POST'])
def new_organization():
    form = OrganizationForm()
    if form.validate_on_submit():
        organization = Organization(name=form.name.data, email=form.email.data, address=form.address.data, phone=form.phone.data)
        db.session.add(organization)
        db.session.commit()
        flash('Your organization has been created!', 'success')
        return redirect(url_for('organization.organizations'))
    return render_template('create_organization.html', title='New Organization', form=form, legend='New Organization')

@organization.route('/organization/<int:organization_id>')
def organization_details(organization_id):
    organization = Organization.query.get_or_404(organization_id)
    return render_template('organization.html', title=organization.name, organization=organization)

@organization.route('/organization/<int:organization_id>/update', methods=['GET', 'POST'])
def update_organization(organization_id):
    organization = Organization.query.get_or_404(organization_id)
    form = OrganizationForm()
    if form.validate_on_submit():
        organization.name = form.name.data
        organization.email = form.email.data
        organization.address = form.address.data
        organization.phone = form.phone.data
        db.session.commit()
        flash('Your organization has been updated!', 'success')
        return redirect(url_for('organization.organization_details', organization_id=organization.id))
    elif request.method == 'GET':
        form.name.data = organization.name
        form.email.data = organization.email
        form.address.data = organization.address
        form.phone.data = organization.phone
    return render_template('create_organization.html', title='Update Organization', form=form, legend='Update Organization')

@organization.route('/organization/<int:organization_id>/delete', methods=['POST'])
def delete_organization(organization_id):
    organization = Organization.query.get_or_404(organization_id)
    db.session.delete(organization)
    db.session.commit()
    flash('Your organization has been deleted!', 'success')
    return redirect(url_for('organization.organizations'))

@organization.route('/organizations')
def organizations():
    organizations = Organization.query.all()
    return render_template('organizations.html', organizations=organizations)