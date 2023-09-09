from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, URL, Optional

class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired(), URL()])
    source = StringField('Source', validators=[Optional()])
    publication_date = DateTimeField('Publication Date (yyyy-mm-dd hh:mm:ss)', format='%Y-%m-%d %H:%M:%S', validators=[Optional()])
    summary = TextAreaField('Summary', validators=[Optional()])
    submit = SubmitField('Submit')
