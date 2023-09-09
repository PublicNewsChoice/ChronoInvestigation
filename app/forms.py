from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Email, Length, Optional
# Remove the import of db and action_articles_association from this file


class OrganizationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    address = StringField('Address', validators=[Optional(), Length(max=200)])
    email = StringField('Email', validators=[Optional(), Email(), Length(max=100)])
    phone = StringField('Phone', validators=[Optional(), Length(max=20)])
    submit = SubmitField('Submit')


class EventForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    date = DateTimeField('Date', validators=[DataRequired()])
    # ... (add other fields as needed)
    submit = SubmitField('Submit')


class PersonForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    # ... (add other fields as needed)
    submit = SubmitField('Submit')


class ActionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[Optional(), Length(max=500)])
    # ... (add other fields as needed)
    submit = SubmitField('Submit')


class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired(), Length(max=255)]) # URL field added
    source = StringField('Source', validators=[Optional(), Length(max=255)]) # Source field added
    publication_date = DateTimeField('Publication Date', validators=[Optional()], default=datetime.utcnow) # Publication Date field added
    summary = TextAreaField('Summary', validators=[Optional()]) # Summary field added
    submit = SubmitField('Submit')
