from app import db
from app.models.organization import Organization

def create_organization(data):
    new_organization = Organization(
        #... populate with necessary fields from data
    )
    db.session.add(new_organization)
    db.session.commit()
    return new_organization

def get_organization_by_id(organization_id):
    return Organization.query.get(organization_id)

def get_all_organizations():
    return Organization.query.all()

def update_organization(organization_id, data):
    organization = Organization.query.get(organization_id)
    if organization:
        #... update fields with data
        db.session.commit()
        return organization
    return None

def delete_organization(organization_id):
    organization = Organization.query.get(organization_id)
    if organization:
        db.session.delete(organization)
        db.session.commit()
        return organization
    return None